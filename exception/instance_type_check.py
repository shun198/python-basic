class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name}は歩きます")


def walk_with_me(animal):
    animal.walk()
