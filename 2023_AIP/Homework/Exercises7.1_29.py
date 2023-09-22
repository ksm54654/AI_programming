from fraction import Fraction

def main():
    number = input("Enter a positive decimal number less than 1 : ")

    if number[0] == '0':
        precision = len(number[2:])
    elif number[0] == '.':
        per
    else:
        return 

    numer = 
    denom = 


    frac = Fraction(numer, denom)
    try:
        numer_reduced, denom_reduced = frac.reduce()

        if denom_reduced == 1:
            print('Reduction : {}'.format(numer_reduced))
        else:
            print('Reduction : {} / {}'.format(numer_reduced, denom_reduced))
    except Exception as exp:
        print(exp)

main()