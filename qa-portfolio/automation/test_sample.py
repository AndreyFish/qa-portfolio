import pytest

def add(x, y):
    return x + y

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -3) == -4
