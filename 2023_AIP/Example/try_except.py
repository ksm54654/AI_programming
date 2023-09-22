def func1():
    try:
        print('func1')
        raise ZeroDivisionError
    except AttributeError as e:
        print(e)

def func2():
    try:
        print('func2')
        func1()
    except ZeroDivisionError as e:
        print(e)

def main():
    # func1()
    try:
        func2()
    except AttributeError as e:  # AttributeError -> Exception해도됨ㅇ.ㅇ
        print(e)

main()