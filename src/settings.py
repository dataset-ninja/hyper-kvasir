from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "HyperKvasir"
PROJECT_NAME_FULL: str = "HyperKvasir: The Largest Gastrointestinal Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [
    AnnotationType.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [
    AnnotationType.InstanceSegmentation(),
    AnnotationType.ObjectDetection(),
]

RELEASE_DATE: Optional[str] = "2020-08-28"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None
HOMEPAGE_URL: str = "https://datasets.simula.no/hyper-kvasir/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 865838
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/hyper-kvasir"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://datasets.simula.no/downloads/hyper-kvasir/hyper-kvasir-segmented-images.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.nature.com/articles/s41597-020-00622-y"
CITATION_URL: Optional[str] = "https://datasets.simula.no/hyper-kvasir/"
AUTHORS: Optional[List[str]] = [
    "Hanna Borgli",
    "Vajira Thambawita",
    "Pia H. Smedsrud",
    "Steven Hicks",
    "Debesh Jha",
    "Sigrun L. Eskeland",
    "Kristin Ranheim Randel",
    "Konstantin Pogorelov",
    "Mathias Lux",
    "Duc Tien Dang Nguyen",
    "Dag Johansen",
    "Carsten Griwodz",
    "Håkon K. Stensland",
    "Enrique Garcia-Ceja",
    "Peter T. Schmidt",
    "Hugo L. Hammer",
    "Michael A. Riegler",
    "Pål Halvorsen",
    "Thomas de Lange",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "NO-SW-AU joint research group"
ORGANIZATION_URL: Optional[
    Union[str, List[str]]
] = "https://www.nature.com/articles/s41597-020-00622-y#author-information"
SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
