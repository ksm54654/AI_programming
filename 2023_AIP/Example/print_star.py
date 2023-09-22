numberOfRows = int(input('Enter a number from 1 to 20: '))

for i in range(numberOfRows):
    for j in range(i + 1):
        print('*', end='')
    for k in range(numberOfRows - (i + 1)):
        print('+' ,end='')
    print()

for i in range(numberOfRows):
    for k in range(numberOfRows - (i + 1)):
        print('*', end='')
    for j in range(i + 1):
        print('+' ,end='')
    print()