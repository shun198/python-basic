# 華氏から接氏へ変換
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


celsius = fahrenheit_to_celsius(59)
# print(celsius)


def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


avg = get_average(1, 2, 3, 4, 5)
# print(avg)


def kwargs_function(**kwargs):
    print(kwargs)


kwargs_function(a=1, b=2, c=3)
