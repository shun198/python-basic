import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # クラスメソッドからインスタンスメソッドを作るのをファクトリメソッドと呼ぶ
    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        return cls(name=name, age=age)


john = Person("John", 23)
print(john.name)
