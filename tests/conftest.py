import pytest

@pytest.fixture
def sample_data():
    return {
        "a": 10,
        "b": 5,
        "expected_sum": 15,
        "expected_difference": 5,
        "expected_product": 50,
        "expected_quotient": 2.0,
    }