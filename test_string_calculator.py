import pytest
from string_calculator import add


def test_empty_string_returns_zero():
    """Test that empty string returns 0"""
    assert add("") == 0


def test_single_number_returns_that_number():
    """Test that single number returns that number"""
    assert add("1") == 1


def test_two_comma_separated_numbers_returns_sum():
    """Test that two comma-separated numbers return their sum"""
    assert add("1,5") == 6


def test_multiple_comma_separated_numbers_returns_sum():
    """Test that multiple comma-separated numbers return their sum"""
    assert add("1,2,3,4") == 10


def test_newline_as_separator():
    """Test that newlines can be used as separators"""
    assert add("1\n2,3") == 6


def test_custom_delimiter():
    """Test custom delimiter format: //[delimiter]\n[numbers...]"""
    assert add("//;\n1;2") == 3
