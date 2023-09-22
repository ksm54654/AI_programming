# import numeric
from problem import Numeric

def main():
    # Create an instance of numerical optimization problem
    p = Numeric()
    p.setVariables()
    # Call the search algorithm
    solution, mininum = gradientDescent(p)
    # Show the problem and algorithm settings
    p.storeResult(solution, mininum)
    p.describe()
    displaySetting(p)
    # Report results
    p.report()

def gradientDescent(p):
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current) # 현재 함수값
    while True:
        successor = p.takeStep(current, valueC)
        valueS = p.evaluate(successor)
        if valueS >= valueC: # 후보값이 현재보다 크거나 같으면 
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def displaySetting(p):
    print()
    print("Search algorithm: Gradient-descent Hill Climbing")
    print()
    print("step size:", p.getAlpha())

main()
