import pytest
from math_utils import add, divide, average


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (2.5, 0.5, 3.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_average_list():
    assert average([2, 4, 6]) == 4


def test_average_empty():
    with pytest.raises(ValueError):
        average([])
