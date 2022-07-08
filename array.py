import array as arr

arr = arr.array("i", [1, 2, 3, 4, 5])
print(arr[0])
print(arr[-1])
print(arr[-2]/2)

# データ型がバラバラだとエラーが発生する
# ram_arr = arr.array("i", [1, True, "aaa", 4, 5])
# print(ram_arr[2])
