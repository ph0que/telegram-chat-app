import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)  # глобальный клиент

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Telegram Chat API is running"}

def test_get_messages_initial():
    resp = client.get("/messages")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 3
    first = data[0]
    assert {"id", "text", "fromMe", "timestamp"} <= set(first.keys())

def test_create_message():
    payload = {"text": "test message", "fromMe": True}
    resp = client.post("/messages", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["text"] == "test message"
    assert data["fromMe"] is True
    assert "id" in data
    assert "timestamp" in data

def test_messages_list_grows_after_post():
    resp_before = client.get("/messages")
    count_before = len(resp_before.json())
    
    client.post("/messages", json={"text": "another msg", "fromMe": False})
    
    resp_after = client.get("/messages")
    count_after = len(resp_after.json())
    
    assert count_after == count_before + 1
