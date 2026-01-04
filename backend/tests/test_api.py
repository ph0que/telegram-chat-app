import pytest


def test_simple_addition():
    """Simple test to verify pytest is working"""
    assert 2 + 2 == 4


def test_string_equality():
    """Test string equality"""
    assert "hello".upper() == "HELLO"


def test_list_operations():
    """Test list operations"""
    items = [1, 2, 3, 4, 5]
    assert len(items) == 5
    assert sum(items) == 15
