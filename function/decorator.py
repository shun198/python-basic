def greeting(func):
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Nice to meet you")
    return inner


@greeting
def say_name(name):
    print(f"My name is {name}")


@greeting
def say_name_and_age(name, age):
    print(f"My name is {name} and I am {age} years old")


say_name("Taro")
say_name_and_age("Hanako", 20)
