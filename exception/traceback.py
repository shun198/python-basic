import traceback


def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        traceback.print_exc()
        print("0で割ることができません。正しい値を入力してください")
    else:
        print(f"1人あたり{each}円")


def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        traceback.print_exc()
        print("文字列ではなく、数字を入力してください")


if __name__ == "__main__":
    bill = {'burger': 500, 'cola': 120, 'fries': 150}
    check(bill)
