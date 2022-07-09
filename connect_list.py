a = [1, 4, 7]
b = [10, 13, 16]
c = a + b
print(c)
a.append(b)
print(a)

list = ["This", "is", "a", "list"]
print(" ".join(list))
print("/".join(list))

excel = "excel.xlsx"
print(excel.split("."))
# ファイル名を取得
print(excel.split(".")[0])
# 拡張子を取得
print(excel.split(".")[-1])
