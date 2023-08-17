Dataset **HyperKvasir Segmentation** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/p/r/WQ/Ffj4Hqm0IhFziRsIJP4td5K3hCTZ73TMnsmRyc2Gzx0YI2RoB1C7NeYVXtQLpSjQyk0NTJNjAqOmW0WlNWQ22AwEel7DKT9mKJntHPiPq4PAhUc22m1fk4eveXgf.tar)

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