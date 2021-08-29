import time
from concurrent.futures import ThreadPoolExecutor
import asyncio

pool = ThreadPoolExecutor(8)


class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup)
        except Exception as e:
            print(e)

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)


def recursive(n):
    yield pool.submit(time.sleep, 0.001)
    Task(recursive(n + 1)).step()
    print(n)


def loop():
    while True:
        item = yield
        print(item)


if __name__ == '__main__':
    main_loop = loop()
    next(main_loop)
    main_loop.send('asdasds')

    func = recursive(1)
    print(func)
    Task(func).step()
