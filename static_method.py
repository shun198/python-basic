class MyClass(object):

    def my_method(self):
        print('This is my method')

    @staticmethod
    def my_static_method():
        print('This is my static method')


# インスタンスを作成
c = MyClass()
c.my_method()
# スタティックメソッドを呼び出す
# インスタンスを作成しないで呼び出すこともできる
MyClass.my_static_method()
