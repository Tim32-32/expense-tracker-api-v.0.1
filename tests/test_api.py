from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Тест регистрации
def test_register_user():
    response = client.post("/users/register", json={
        "email": "test@example.com",
        "password": "strongpassword"
    })
    assert response.status_code == 201 or response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == "test@example.com"


def test_add_expense_unauthorized():
    response = client.post("/expenses/", json={
        "amount": 100,
        "category": "food",
        "description": "Обед в ресторане"
    })
    assert response.status_code == 401  # Потому что не передан токен авторизации
