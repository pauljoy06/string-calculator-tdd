import pytest
from string_calculator import add


def test_empty_string_returns_zero():
    """Test that empty string returns 0"""
    assert add("") == 0


def test_single_number_returns_that_number():
    """Test that single number returns that number"""
    assert add("1") == 1