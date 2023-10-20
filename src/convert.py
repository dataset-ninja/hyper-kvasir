# https://datasets.simula.no/hyper-kvasir/

import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely.io.fs import (
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    list_files_recursively,
)
from supervisely.io.json import load_json_file

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()

# project_name = "HyperKvasir"
dataset_path = "/home/grokhi/rawdata/hyper-kvasir"

batch_size = 100

images_folder = "images"
masks_folder = "masks"
bbox_json_name = "bounding-boxes.json"

img_ext = '.jpg'


def fix_masks(image_np: np.ndarray) -> np.ndarray:
    lower_bound = np.array([200, 200, 200])
    upper_bound = np.array([255, 255, 255])
    condition_white = np.logical_and(
        np.all(image_np >= lower_bound, axis=2), np.all(image_np <= upper_bound, axis=2)
    )

    lower_bound = np.array([1, 1, 1])
    upper_bound = np.array([100, 100, 100])
    condition_black = np.logical_and(
        np.all(image_np >= lower_bound, axis=2), np.all(image_np <= upper_bound, axis=2)
    )

    image_np[np.where(condition_white)] = (255, 255, 255)
    image_np[np.where(condition_black)] = (0, 0, 0)

    return image_np



obj_class = sly.ObjClass("polyp", sly.Bitmap)
obj_class_bbox = sly.ObjClass("polyp_bbox", sly.Rectangle)

tag_names = [
    "lower-gi-tract",
    "anatomical-landmarks",
    "cecum",
    "ileum",
    "retroflex-rectum",
    "pathological-findings",    
    "hemorrhoids",
    "polyps",
    "ulcerative-colitis-grade-0-1",
    "ulcerative-colitis-grade-1",
    "ulcerative-colitis-grade-1-2",
    "ulcerative-colitis-grade-2",
    "ulcerative-colitis-grade-2-3",                
    "ulcerative-colitis-grade-3",                             
    "quality-of-mucosal-views",   
    "bbps-0-1",
    "bbps-2-3",                  
    "impacted-stool",
    "therapeutic-interventions",
    "dyed-lifted-polyps",
    "dyed-resection-margins",
    "upper-gi-tract",   
    "pylorus", 
    "retroflex-stomach",   
    "z-line",   
    "barretts", 
    "barretts-short-segment", 
    "esophagitis-a",   
    "esophagitis-b-d",
]
tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]



def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    

    def create_ann(image_path):
        labels, tags = [], []
        
        image_np = sly.imaging.image.read(image_path)[:, :, :]
        image_np = image_np[:, :, 0]        

        if ds_name=='labeled-images':
            tag_names = image_path.split("/")
            tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name in tag_names]
            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), img_tags=tags)
        
        elif ds_name=='unlabeled-images':
            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]))
        
        elif ds_name=='segmented-images':
            mask_path = os.path.join(masks_path, get_file_name_with_ext(image_path))
            mask_np = sly.imaging.image.read(mask_path)[:, :, :]
            mask_np = fix_masks(mask_np)[:, :, 0]
        
            bbox_data = json_ann[get_file_name(image_path)]["bbox"]

            if len(np.unique(mask_np)) != 1:
                if len(bbox_data) > 1:
                    ret, curr_mask = connectedComponents(mask_np.astype("uint8"), connectivity=8)
                    for i in range(1, ret):
                        obj_mask = curr_mask == i
                        bitmap = sly.Bitmap(obj_mask)
                        if bitmap.area < 100:
                            continue
                        label = sly.Label(bitmap, obj_class)
                        labels.append(label)
                else:
                    obj_mask = mask_np == 255
                    bitmap = sly.Bitmap(obj_mask)
                    label = sly.Label(bitmap, obj_class)
                    labels.append(label)

            for curr_bbox in bbox_data:
                rectangle = sly.Rectangle(
                    top=curr_bbox["ymin"],
                    left=curr_bbox["xmin"],
                    bottom=curr_bbox["ymax"],
                    right=curr_bbox["xmax"],
                )
                label = sly.Label(rectangle, obj_class_bbox)
                labels.append(label)

            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), labels=labels)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class, obj_class_bbox], tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ["labeled-images" , "segmented-images" , "unlabeled-images"]:

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_path = os.path.join(dataset_path, ds_name, images_folder) if ds_name != "labeled-images" else os.path.join(dataset_path, ds_name)
        masks_path = os.path.join(dataset_path, ds_name, masks_folder)
        images_paths = [path for path in list_files_recursively(images_path) if path.endswith(img_ext)]

        if ds_name=="segmented-images":
            json_path = os.path.join(dataset_path,ds_name, bbox_json_name)
            json_ann = load_json_file(json_path)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_paths))

        for images_paths_batch in sly.batched(images_paths, batch_size=batch_size):
            img_names_batch = [
                get_file_name_with_ext(image_path) for image_path in images_paths_batch
            ]

            anns_batch = [
                create_ann(image_path) for image_path in images_paths_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_paths_batch)
            img_ids = [im_info.id for im_info in img_infos]

            api.annotation.upload_anns(img_ids, anns_batch)

            progress.iters_done_report(len(images_paths_batch))

    return project
