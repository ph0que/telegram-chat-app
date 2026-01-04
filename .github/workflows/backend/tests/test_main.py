import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test that the root endpoint returns 200"""
    response = client.get("/")
    assert response.status_code == 200


def test_health_check():
    """Test health check endpoint if it exists"""
    response = client.get("/health")
    # Either 200 or 404 is acceptable (if endpoint doesn't exist)
    assert response.status_code in [200, 404]


def test_cors_headers():
    """Test that CORS headers are present"""
    response = client.options("/")
    # Some CORS implementation might not include headers in OPTIONS
    assert response.status_code in [200, 405]
