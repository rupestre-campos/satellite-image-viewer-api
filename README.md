
# Geospatial API

One stop shop for automatized image collection


## satellite image viewer
Simple endpoint to get sentinel2 satellite images

## Instalation
How to run in debian based linux distros
Recomended Python version: Python 3.10 or above

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd src/
uvicorn main:app --reload
```

## Development
How to run tests
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt

# run tests
pytest tests/
```

## Docker build

```
docker build -t sat-img-view-api .
docker run -d --name sat-img-view-api-container -p 8000:8000 sat-img-view-api
docker start sat-img-view-api-container
```