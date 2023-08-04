The **HyperKvasir** dataset can be split into four distinct parts: *labeled* image data, *unlabeled* image data, *segmented* image data, and *annotated* video data. Following dataset contains **segmented image data**.

Artificial intelligence has gained significant attention in the medical field, but obtaining medical data for training AI models is challenging due to legal restrictions and the labor-intensive process of manual data labeling. The authors address this issue by presenting HyperKvasir, the largest image and video dataset of the gastrointestinal tract.

The authors highlight the importance of improving endoscopic performances and clinical examinations to prevent GI disease-related morbidity and deaths. They also emphasize the promising role of AI-enabled support systems in delivering quality healthcare at a large scale.

The images and videos in the HyperKvasir dataset were collected prospectively during routine clinical examinations at a Norwegian hospital from 2008 to 2016. The dataset initially contained 4,000 labeled images, later extended to 8,000 images. The Kvasir dataset, consisting of these labeled images, has been widely used by researchers worldwide to develop various machine learning models and AI systems for GI endoscopy.

Regarding the set of segmented images, the authors provide the original image, a segmentation mask, and a bounding box for 1,000 images from the *polyp* class. The segmentation mask represents the region of interest, i.e., polyp tissue, with foreground pixels depicted in white and background pixels in black. The bounding box outlines the outermost pixels of the found *polyp*.
