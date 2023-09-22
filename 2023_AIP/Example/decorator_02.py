def trace(func):
    def wrapper(a, b):
        r = func(a, b)
        print(f'a={a}, b={b} -> r={r}')
        return r
    return wrapper

@trace
def add(a, b):
    return a + b

print(add(10, 20))