# import numeric
from numeric import *

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain) ()=>는 튜플.
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC: # 후보값이 현재보다 크거나 같으면 
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): ###
    neighbors = []
    for i in range(len(current)):
        mutant = mutate(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, DELTA, p)
        neighbors.append(mutant)

    return neighbors     # Return a set of successors

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best, p)

    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue: # 좋은거. 새로운 값을 찾은거
            best = neighbors[i]
            bestValue = newValue

    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
