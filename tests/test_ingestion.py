import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ingestion_success():

    response = client.post(
        "/ingest/",
        json={
            "endpoints": [
                "https://dummyjson.com/products"
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert "saved_records" in data


def test_invalid_api_url():

    response = client.post(
        "/ingest/",
        json={
            "endpoints": [
                "https://wrong-url-example.com"
            ]
        }
    )

    assert response.status_code == 400

    data = response.json()

    assert "detail" in data