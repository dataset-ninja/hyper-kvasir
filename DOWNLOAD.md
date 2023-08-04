Dataset **HyperKvasir Segmentation** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/v/bq/5HI7RAQcHMvhN7AcGGQa1mqcqX9QrEO4KMURm0F7zmGCsRI7Csb9vx7sAV38DLBLKgx0oSgKNGGJeRpbLEPdVybtK61OabaHc4Gn8eC7EOGVxsoAPPgTlGkSM7Xd.tar)

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

The data in original format can be [downloaded here](https://datasets.simula.no/downloads/hyper-kvasir/hyper-kvasir-segmented-images.zip)