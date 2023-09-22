def displaySequenceOfNumbers(m, n):
    while m <= n:
        print(m, end = ' '
              
              )
        m = m + 1

def displaySequenceOfNumbersRecursion(m, n):
    if m > n:
        return
    elif m == n:
        print(m, end = ' ')
    else:
        print(m, end = ' ')
        displaySequenceOfNumbersRecursion(m + 1, n)


displaySequenceOfNumbers(5, 10)
print('')
displaySequenceOfNumbersRecursion(5, 10)
print('')
