import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Telegram Chat API is running"}


@pytest.mark.asyncio
async def test_get_messages_initial():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/messages")
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 3
    first = data[0]
    assert {"id", "text", "fromMe", "timestamp"} <= set(first.keys())


@pytest.mark.asyncio
async def test_create_message():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"text": "test message", "fromMe": True}
        resp = await ac.post("/messages", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["text"] == "test message"
    assert data["fromMe"] is True
    assert "id" in data
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_messages_list_grows_after_post():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp_before = await ac.get("/messages")
        count_before = len(resp_before.json())

        await ac.post("/messages", json={"text": "another msg", "fromMe": False})

        resp_after = await ac.get("/messages")
        count_after = len(resp_after.json())

    assert count_after == count_before + 1
