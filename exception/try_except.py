def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることができません。正しい値を入力してください")
        print(e)
    except ValueError as e:
        print("文字列ではなく、数字を入力してください")
        print(e)
    else:
        print(f"1人あたり{each}円")
    finally:
        print("処理が終了しました")


if __name__ == "__main__":
    split_bill(10000)
