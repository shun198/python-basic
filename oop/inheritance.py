class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Animal constructor is called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def __init__(self, name):
        # super()で親クラスのコンストラクタを呼び出す
        super().__init__(name=name)
        print("Dog constructor is called")

    # オーバーライド
    def breath(self):
        print("breath method is overrided")
        return super().breath()


class Cat(Animal):
    pass


pochi = Dog('pochi')
tama = Cat('tama')
print(pochi.name)
pochi.breath()
print(tama.name)
tama.breath()
