Dataset **HyperKvasir Segmentation** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/U/T/Ko/SHwNA3Wc6WIWRA8tIZoxmzrapCSomnmqeVCvwAxsPufX6wKt7861UvbeIxgSPsvkVZZGsqf3kjnmwggmPKDA7UvN1uMQSxeav5T8i4PpLZiviCkxgvEf4FnEwOfL.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='HyperKvasir Segmentation', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://datasets.simula.no/downloads/hyper-kvasir/hyper-kvasir-segmented-images.zip).