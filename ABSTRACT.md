The authors address the prominence of artificial intelligence in the medical field, specifically in the context of sparse medical data due to legal restrictions and the labor-intensive nature of labeling training data. They present the **HyperKvasir** dataset, which is currently the most extensive collection of images and videos related to the gastrointestinal tract. This dataset, comprising 110,079 images and 374 videos, was obtained from real gastro- and colonoscopy examinations at Bærum Hospital in Norway and partially labeled by experienced gastrointestinal endoscopists. The dataset encompasses a variety of anatomical landmarks, normal findings, and pathological conditions. The combined image and video frames amount to approximately 1 million.

The human gastrointestinal (GI) tract experiences a range of mucosal abnormalities, including benign and life-threatening diseases. GI cancers, in particular, contribute to a significant global health burden. Endoscopy serves as the gold-standard diagnostic tool for GI tract examination, but its effectiveness is influenced by the variability in operator performance. Improved endoscopic outcomes are crucial for preventing GI-related morbidity and mortality, and artificial intelligence (AI) support systems have shown promise in enhancing endoscopic performance.

<img src="https://github.com/supervisely/dataset-tools/assets/78355358/ec225a53-40ce-4ce0-8b6f-c456d0feb765" alt="image" width="800">

However, AI-based solutions require large, well-labeled datasets for training machine learning models. Obtaining such datasets in the medical domain is challenging due to legal constraints and data collection difficulties. Despite these challenges, AI-based diagnostic tools for endoscopy are emerging.

To address these limitations, the authors introduced the HyperKvasir dataset. This dataset comprises images and videos collected from routine clinical examinations at a Norwegian hospital between 2008 and 2016. The images were obtained from the Picsara image documentation database. The dataset was progressively expanded and used by researchers worldwide to develop various AI models for GI endoscopy.

The dataset contains *labeled-images*, *segmented-images*, and *unlabeled-images*. Labeled images are categorized based on the location in the GI tract, the quality of mucosal views, pathological findings, and therapeutic interventions. The lower GI tract is examined during colonoscopy, including the terminal ileum, colon, and rectum, while the upper GI tract includes the esophagus, stomach, and duodenum.

<img src="https://github.com/supervisely/dataset-tools/assets/78355358/db57b85f-b92c-4998-a573-738c2bd40bcf" alt="image" width="800">

<img src="https://github.com/supervisely/dataset-tools/assets/78355358/1a032386-1337-4a8e-84c1-04407e80fb90" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">The various image classes structured under position and type, also the structure of the stored images.</span>

For the lower GI tract, the dataset includes anatomical landmarks, bowel preparation quality, and various pathological findings such as ulcerative colitis, polyps, and hemorrhoids. Therapeutic interventions, such as polyp removal and ulcer injection, are also covered.

In the upper GI tract, the dataset features anatomical landmarks and pathological findings, including reflux esophagitis and Barrett's esophagus.

The unlabeled images are provided for further research and analysis.

In summary, the HyperKvasir dataset offers a valuable resource for developing AI-based diagnostic tools for endoscopy, particularly for the gastrointestinal tract. The dataset is open access and freely available to researchers, supporting advancements in the field of medical AI.