# 状態をキープした関数を作成できる
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(2))
print(power_four(3))


def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
