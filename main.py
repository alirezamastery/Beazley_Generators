_registry = dict()


def actor(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        _registry[func.__name__] = gen

    return wrapper


def send(name, msg):
    _registry[name].send(msg)


@actor
def printer():
    while True:
        item = yield
        print('Got:', item)


printer()


@actor
def ping():
    while True:
        msg = yield
        print('ping:', msg)
        send('pong', msg + 1)


@actor
def pong():
    while True:
        msg = yield
        print('pong:', msg)
        send('ping', msg + 1)


ping()
pong()

send('ping',0)
