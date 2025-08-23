import pytest
from string_calculator import add


def test_empty_string_returns_zero():
    """Test that empty string returns 0"""
    assert add("") == 0