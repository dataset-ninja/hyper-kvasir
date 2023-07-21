Dataset **HyperKvasir (segmentation)** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/s/X/63/G4tRz4GQrSkIuvJwoRJAIY4XeWgZWfdTxdl2ZzLpoVUVHE9ApJBpRypAXm58UXJm7h8Q8v9lQN9ktFh37eFGnthe5kZRdDipj6fIVtQ43O1O76OgeZbnmuyEO3dj.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='HyperKvasir (segmentation)', dst_path='~/dtools/datasets/HyperKvasir (segmentation).tar')
```
The data in original format can be 🔗[downloaded here](https://datasets.simula.no/downloads/hyper-kvasir/hyper-kvasir-segmented-images.zip)