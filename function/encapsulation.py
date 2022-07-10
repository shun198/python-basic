# カプセル化(encapsulation) 外部から変更できないようにする
def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f'You are {age} years old.Too young to enter')
        return

    def inner_casino_entrance():
        print("Welcome to the casino")

    inner_casino_entrance()


casino_entrance(18)
# エラーになる(inner_casino_entrance()にはアクセスできない)
# inner_casino_entrance()
