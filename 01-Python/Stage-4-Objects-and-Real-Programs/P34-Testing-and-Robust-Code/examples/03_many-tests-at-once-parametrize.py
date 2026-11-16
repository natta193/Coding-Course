import pytest
from maths import is_leap

@pytest.mark.parametrize("year, expected", [
    (2024, True), (2023, False),
    (1900, False), (2000, True),   # boundaries
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected
