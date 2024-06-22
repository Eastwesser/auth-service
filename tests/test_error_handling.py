import pytest


@pytest.mark.anyio
async def test_404_error(client):
    response = await client.get("/nonexistent-route")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


@pytest.mark.anyio
async def test_invalid_login(client):
    response = await client.post("/auth/login", data={"username": "invaliduser", "password": "invalidpass"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}
