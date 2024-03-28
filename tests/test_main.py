import json
import io
from PIL import Image
import numpy as np
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def stac_item():
    with open("tests/data/stac_item.json") as test_data:
        return json.load(test_data)

@pytest.fixture
def feature_geojson():
    with open("tests/data/polygon_feature.geojson") as test_data:
        return json.load(test_data)

@pytest.fixture
def sample_image():
    with io.BytesIO() as buffer:
        image_data = Image.fromarray(np.zeros(100).astype(np.uint8))
        image_data.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer.getvalue()

@pytest.fixture
def sample_search_request(feature_geojson):
    return {
        "geometry": feature_geojson,
        "parameters": {
            "max_cloud_coverage": 30,
            "start_date": "2023-01-01",
            "end_date": "2024-01-01",
            "max_results": 5
        }
    }

@pytest.fixture
def sample_render_request(stac_item, feature_geojson):
    return {
        "geometry": feature_geojson,
        "parameters": {
            "stac_items": [stac_item],
            "image_format": "PNG"
        }
    }

def test_health(sample_render_request):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert "content-length" in response.headers

def test_search_image(sample_search_request):
    response = client.post("/search-image", json=sample_search_request)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert "content-length" in response.headers

def test_search_image_invalid_date(sample_search_request):
    sample_search_request["parameters"]["start_date"] = 123456
    response = client.post("/search-image", json=sample_search_request)
    assert response.status_code == 400
    assert response.headers["content-type"] == "application/json"
    assert "content-length" in response.headers

def test_render_image(sample_render_request):
    response = client.post("/render-image", json=sample_render_request)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert "content-length" in response.headers

def test_render_image_jpeg(sample_render_request):
    sample_render_request["parameters"]["image_format"] = "JPEG"
    response = client.post("/render-image", json=sample_render_request)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    assert "content-length" in response.headers

def test_render_image_zip_png(sample_render_request):
    sample_render_request["parameters"]["zip_file"] = "Y"
    response = client.post("/render-image", json=sample_render_request)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"
    assert "content-length" in response.headers

def test_render_image_zip_jpeg(sample_render_request):
    sample_render_request["parameters"]["image_format"] = "JPEG"
    sample_render_request["parameters"]["zip_file"] = "Y"
    response = client.post("/render-image", json=sample_render_request)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"
    assert "content-length" in response.headers

def test_render_image_empty_stac_items(sample_render_request):
    sample_render_request["parameters"]["stac_items"] = []
    response = client.post("/render-image", json=sample_render_request)
    assert response.status_code == 400
    assert response.headers["content-type"] == "application/json"
    assert "content-length" in response.headers

def test_render_image_invalid_format(sample_render_request):
    sample_render_request["parameters"]["image_format"] = "WEBP"
    response = client.post("/render-image", json=sample_render_request)
    assert response.status_code == 400
    assert response.headers["content-type"] == "application/json"
    assert "content-length" in response.headers
