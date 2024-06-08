import pytest
from my_module.module1 import my_function


def test_my_function():
    assert my_function(2, 3) == 5


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 2),
        (-1, 1, 0),
    ],
)
def test_my_function_param(a, b, expected):
    assert my_function(a, b) == expected
