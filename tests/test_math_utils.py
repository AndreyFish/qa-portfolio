# test_math_utils.py
from math_utils import add

def test_add_positive_numbers():
    assert add(3, 4) == 7

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5   
    # test_math_utils.py (обновлённый)
import pytest
from math_utils import add

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 7),
    (-2, -3, -5),
    (0, 5, 5)
])
def test_add(a, b, expected):
    assert add(a, b) == expected   