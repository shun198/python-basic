# def square(x):
#     return x * x


# print(square(2))

lambda x: x * x


def power(exponent):
    return lambda base: base ** exponent


power_two = power(3)
print(power_two(2))
