# import numeric
from problem import Numeric

def main():
    # Create an instance of numerical optimization problem
    p = Numeric()
    p.setVariables()
    # Call the search algorithm
    solution, mininum = steepestAscent(p)
    # Show the problem and algorithm settings
    p.storeResult(solution, mininum)
    p.describe()
    displaySetting(p)
    # Report results
    p.report()

def steepestAscent(p):
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC: # 후보값이 현재보다 크거나 같으면 
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def bestOf(neighbors, p): 
    best = neighbors[0]     # 'best' is value lis
    bestValue = p.evaluate(best)

    for i in range(1, len(neighbors)):
        newValue = p.evaluate(neighbors[i])
        if newValue < bestValue: # 좋은거. 새로운 값을 찾은거
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()
