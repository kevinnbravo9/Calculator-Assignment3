import pytest
from app.operations import Operations

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 8),
        (2.5, 4.5, 7.0),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_addition(a, b, expected):
    assert Operations.addition(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (2.5, 4.5, -2.0),
        (-1, 1, -2),
        (0, 0, 0),
    ],
)
def test_subtraction(a, b, expected):
    assert Operations.subtraction(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 15),
        (2.5, 4.5, 11.25),
        (-1, 1, -1),
        (0, 0, 0),
    ],
)
def test_multiplication(a, b, expected):
    assert Operations.multiplication(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 5/3),
        (2.5, 4.5, 2.5/4.5),
        (-1, 1, -1),
        (0, 1, 0),
    ],
)
def test_division(a, b, expected):
    assert Operations.division(a, b) == expected

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.division(5, 0)

def test_operations_with_fixture(sample_data):
    assert Operations.addition(sample_data["a"], sample_data["b"]) == sample_data["expected_sum"]
    assert Operations.subtraction(sample_data["a"], sample_data["b"]) == sample_data["expected_difference"]
    assert Operations.multiplication(sample_data["a"], sample_data["b"]) == sample_data["expected_product"]
    assert Operations.division(sample_data["a"], sample_data["b"]) == sample_data["expected_quotient"]