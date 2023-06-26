Dataset **HyperKvasir** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/n/1/po/yMYRrQ7xuFQldJJeyoMZhLOJKhyVtIRGFhKJrMx3Nji7E08juVY4UX6DmjjZeYQQA8eaGOXBmwjlbfeVAhnejWwAhgChYLrYQoBMQlRglKDm3GAEEHhg8jU96sGR.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='HyperKvasir', dst_path='~/dtools/datasets/HyperKvasir.tar')
```
The data in original format can be 🔗[downloaded here](https://datasets.simula.no/downloads/hyper-kvasir/hyper-kvasir-segmented-images.zip)