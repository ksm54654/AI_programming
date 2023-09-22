def trace(func):
    def wrapper():
        print(func.__name__, '시작')
        func()
        print(func.__name__, '끝')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

# trace_hello = trace(hello)
# trace_world = trace(world)

hello()
world()