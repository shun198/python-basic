class MyClass(object):

    classmethod_count = 0

    def my_method(self):
        print('This is my method')

    # staticmethodにはデコレータ
    @staticmethod
    def my_static_method():
        print('This is my static method')

    # classmethodにはデコレータ
    @classmethod
    def my_class_method(cls):
        cls.classmethod_count += 1
        print(f'This is my class method. Count is {cls.classmethod_count}')


# インスタンスを作成
c = MyClass()
c.my_method()
# スタティックメソッドを呼び出す
# インスタンスを作成しないで呼び出すこともできる
MyClass.my_static_method()
MyClass.my_class_method()
