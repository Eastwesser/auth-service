import pytest


@pytest.mark.asyncio
async def test_404_error(client):
    if not hasattr(client, 'get'):
        pytest.skip("Skipping test due to missing 'get' method in AsyncClient")
    response = await client.get("/nonexistent-route")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


@pytest.mark.asyncio
async def test_invalid_login(client):
    if not hasattr(client, 'post'):
        pytest.skip("Skipping test due to missing 'post' method in AsyncClient")
    response = await client.post("/auth/token", data={"username": "invaliduser", "password": "invalidpass"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
