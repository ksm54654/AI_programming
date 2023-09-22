from problem import *
from optimizer import *

def main():
    p, pType = selectProblem() # pType : 1(numeric) or 2(tsp)
    alg = selectAlgorithm(pType)
    alg.run(p)
    p.describe()
    alg.displaySetting()
    p.report()

def selectProblem():
    print("Select the problem type : ")
    print(" 1. Numeric")
    print(" 2. Tsp")
    pType = int(input("Enter the number : "))

    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    else:
        print("Wrong input!!!")
    
    p.setVariables()
    return p, pType

def selectAlgorithm(pType):
    print()
    print("Select the algorithm : ")
    print(" 1. Steepest Ascent")
    print(" 2. First Choice")
    print(" 3. Gradient Descent")

    aType = int(input("Enter the number : "))

    # dicitionary 사용
    optimizers = {1: 'SteepestAscent()', 2: 'FirstChoice()', 3: 'GradientDescent()'}
    alg = eval(optimizers[aType])

    alg.setVariables(pType)
    return alg

main()