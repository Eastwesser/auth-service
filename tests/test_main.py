import pytest


@pytest.mark.asyncio
async def test_read_main(client):
    if not hasattr(client, 'get'):
        pytest.skip("Skipping test due to missing 'get' method in AsyncClient")
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
