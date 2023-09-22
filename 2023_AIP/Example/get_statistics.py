count = 0
total = 0

print('Enter -1 to terminate entering numbers.')
num = int(input('Enter a nonnegative integer : '))
min_val = num
max_val = num

while num != -1:
    count += 1
    total += num

    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    num = int(input('Enter a nonnegative integer : '))

if count > 0:
    if count >= 5:
        print('{}개다.'.format(count))
    print('Mininum : ', min_val)
    print('Maxinum : ', max_val)
    print('Average : ', total / count)
else:
    print('No nonnegative integers were entered.')
