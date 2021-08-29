import time
from itertools import islice, permutations


l = [i for i in range(1000)]
l2 = [i for i in range(100)]


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('duration:', t2 - t1)
        return res

    return wrapper


def iter_tool():
    g = None
    for x in islice(l, 100, None):
        g = x


def slicing():
    g = None
    for x in l[100:]:
        g = x


@timer
def mutate(length):
    x = None
    iterable = [i for i in range(length)]
    for i in permutations(iterable):
        x = i


for i in range(100):
    print(f'{i}')
    mutate(i)
