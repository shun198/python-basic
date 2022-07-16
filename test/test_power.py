from operator import imod


from power import power


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8, "2 ** 3 is 8"


if __name__ == "__main__":
    test_power()
    print("All tests passed")
