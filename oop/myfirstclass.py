class Person:
    # クラス変数。クラスのトップレベルで定義される。
    num_legs = 2
    # __init__はクラスのコンストラクタ(クラスのインスタンスを作成する時に呼ばれる関数)
    # selfはクラスのインスタンスを指す
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} is walking")


# インスタンスを作成
john = Person("John", 23, "male")
kate = Person("Kate", 18, "female")
# インスタンス変数(インスタンスの後ろに.を入れると呼び出せる)
print(john.name)
print(john.age)
# インスタンスメソッド
john.walk()
kate.walk()
# クラス変数
print(john.num_legs)
