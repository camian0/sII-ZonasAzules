import pytest
from fastapi.testclient import TestClient
from main import app
from .setupDB import override_get_db
from config.dB import getDb
from schemas.pageSchema import PageSchema

client = TestClient(app)
app.dependency_overrides[getDb] = override_get_db


# def test_list_blue_zones():
#     page = PageSchema()
#     page.page = 1
#     page.sizePage = 10

#     response = client.get(f"/blue-zone?{page}")
#     print(response)
#     # assert response.status_code == 200
#     # assert response.json() == {"message": "No hay zonas azules para mostrar."}


def test_list_blue_zones_failed():
    response = client.get("/blue-zone")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}
