import os

import pytest
from httpx import AsyncClient

from main import app

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")


@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(app=app, base_url=TEST_DATABASE_URL) as client:
        response = await client.post("/auth/register", json={"username": "testuser", "password": "testpass"})
        assert response.status_code == 200
        assert "username" in response.json()


@pytest.mark.anyio
async def test_login_user(client):
    response = await client.post("/auth/token", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.anyio
async def test_access_protected_route(client):
    login_response = await client.post("/auth/token", data={"username": "testuser", "password": "testpass"})
    token = login_response.json()["access_token"]
    response = await client.get("/protected-route", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "This is a protected route"}
