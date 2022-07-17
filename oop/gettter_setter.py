class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print("get_age called")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age called")
        if age <= 0:
            print("ageは0以上の数値を入力してください")
        else:
            self._age = age


john = Person('John', 30)
print(john.age)
john.age = -10
john.age = 20
print(john.age)
