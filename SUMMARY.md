**HyperKvasir: The Largest Gastrointestinal Dataset** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the medical industry.

The dataset consists of 1000 images with 2133 labeled objects belonging to 2 different classes including *polyp* and *polyp_bbox*.

Images in the HyperKvasir dataset have pixel-level instance segmentation and bounding box annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation task (only one mask for every class). All images are labeled (i.e. with annotations). There is 1 split in the dataset: *ds0* (1000 images). The dataset was released in 2020 by the [NO-SW-AU joint research group](https://www.nature.com/articles/s41597-020-00622-y#author-information).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/hyper-kvasir/raw/main/visualizations/horizontal_grid.png">
