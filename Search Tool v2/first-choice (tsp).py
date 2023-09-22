from problem import Tsp

LIMIT_STUCK = 100  # Max number of evaluation enduring no improvement

def main():
    # Create an instance of TSP
    p = Tsp()    # 'p': (numCities, locations, distanceTable)
    # Call the search algorithm
    p.setVariables()
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    p.storeResult(solution, minimum)
    p.describe()
    displaySetting()
    # Report results
    p.report()
    
def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print("Max evaluations with no improvement: {0:,} iterations"
          .format(LIMIT_STUCK))

main()