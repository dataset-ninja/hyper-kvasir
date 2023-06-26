# https://datasets.simula.no/hyper-kvasir/

import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely.io.fs import get_file_name
from supervisely.io.json import load_json_file

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()

# project_name = "HyperKvasir"
dataset_path = "./APP_DATA/segmented-images"
ds_name = "ds0"
batch_size = 30
download_bbox = True
images_folder = "images"
masks_folder = "masks"
bbox_json_name = "bounding-boxes.json"


def create_ann(image_name, masks_path, json_ann):
    labels = []

    mask_path = os.path.join(masks_path, image_name)
    bbox_data = json_ann[get_file_name(image_name)]["bbox"]

    image_np = sly.imaging.image.read(mask_path)[:, :, 0]
    if len(np.unique(image_np)) != 1:
        if len(bbox_data) > 1:
            ret, curr_mask = connectedComponents(image_np.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                bitmap = sly.Bitmap(obj_mask)
                if bitmap.area < 100:
                    continue
                label = sly.Label(bitmap, obj_class)
                labels.append(label)
        else:
            obj_mask = image_np == 255
            bitmap = sly.Bitmap(obj_mask)
            label = sly.Label(bitmap, obj_class)
            labels.append(label)

    if download_bbox is True:
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


obj_class = sly.ObjClass("polyp", sly.Bitmap)
obj_class_collection = sly.ObjClassCollection([obj_class])
if download_bbox is True:
    obj_class_bbox = sly.ObjClass("polyp_bbox", sly.Rectangle)
    obj_class_collection = sly.ObjClassCollection([obj_class, obj_class_bbox])


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, images_folder)
    masks_path = os.path.join(dataset_path, masks_folder)
    images_names = os.listdir(images_path)
    json_path = os.path.join(dataset_path, bbox_json_name)
    json_ann = load_json_file(json_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        anns_batch = [
            create_ann(image_name, masks_path, json_ann) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(images_names_batch))

    return project
