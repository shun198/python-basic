# assert
import re


a = 1
b = 2
assert a + b == 3, "a + b is equal to 3"


def power(base, exp):
    return base ** exp


assert power(2, 2) == 4, "2 ** 2 is 4"
