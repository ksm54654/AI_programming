x = 50

# def func(x):
#     print('x is', x)
#     x = 2
#     print('x is now', x)

# func(x)
# print('Global x is', x)


# def main():
#     x = 2
#     print(str(x) + 'in main')
#     trivial()
#     print(str(x) + 'in main')

# def trivial():
#     x = 3
#     print(str(x) + 'in trivial')

# main()

def main():
    func()
    print('x : ', x)

def func():
    global x 
    print('x is', x)
    x = 10
    print('x is now', x)

print('Global x before main : ', x)
main()
print('Global x after main : ', x)