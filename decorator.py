import time


def decor(func):
    print('this part before wrapper executes when the code runs even'
          ' if the decorated function is not called at all in the code')

    def wrapper(*args, **kwargs):
        print('in wrapper')
        result = func(*args, **kwargs)
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('duration:', t2 - t1)
        return result

    return wrapper


@decor
def a():
    print('from a')


@decor
def b():
    print('from b')


class C:
    def __init__(self):
        self.x = 10

    def method_one(self):
        print(f'from method_one')

    def method_two(self):
        print(f'from method_two: {self.x}')


class B:
    def __init__(self):
        print(self.__class__)
        self.__class__ = C  # but __init__ of class 'C' wont run
        print(self.__class__)


b = B()
b.method_one()
b.method_two()
