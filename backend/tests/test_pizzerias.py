from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to AI Pizza API"}


def test_get_all_pizzerias():
    response = client.get("/pizzerias")
    assert response.status_code == 200

    pizzerias = response.json()
    assert isinstance(pizzerias, list)
    assert len(pizzerias) >= 1


def test_pizzeria_has_required_fields():
    response = client.get("/pizzerias")
    assert response.status_code == 200

    pizzerias = response.json()
    assert len(pizzerias) > 0

    pizzeria = pizzerias[0]
    assert "id" in pizzeria
    assert "name" in pizzeria
    assert "address" in pizzeria


def test_pizzeria_data_types():
    response = client.get("/pizzerias")
    pizzerias = response.json()

    for pizzeria in pizzerias:
        assert isinstance(pizzeria["id"], int)
        assert isinstance(pizzeria["name"], str)
        assert isinstance(pizzeria["address"], str)
        if pizzeria.get("rating") is not None:
            assert isinstance(pizzeria["rating"], (int, float))
