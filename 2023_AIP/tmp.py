number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Good')
elif guess < number:
    print('higher')
else:
    print('lower')

print('done')