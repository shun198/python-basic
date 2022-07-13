import pytest
from power import power, times


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8, "2 ** 3 is 8"
    with pytest.raises(TypeError):
        power("3", "2")


def test_times():
    a = 1
    b = 2
    assert a * b == 2, "a * b is equal to 2"
