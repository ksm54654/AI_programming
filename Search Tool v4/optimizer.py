from setup import Setup

class HillClimbing:
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._limitStuck = 100

        self._numExp = 0
        self._numRestart = 0

    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pType = parameters['pType']
        self._limitStuck = parameters['limitStuck']
        self._numExp = parameters['numExp']
        self._numRestart = parameters['numRestart']

    def getNumExp(self):
        return self._numExp

    def run(self):
        pass

    def randomRestart(self, p):
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()
        numEval = p.getNumEval()

        for i in range(1, self._numRestart):
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()
            numEval += p.getNumEval()
            if newMinimum < bestMinimum:
                bestMinimum = newMinimum
                bestSolution = newSolution
        p.storeResult(bestSolution, bestMinimum)

    def displaySetting(self):
        if self._pType == 1:
            print()
            print("Mutation step size : ", self._delta)

    def displayNumExp(self):
        print()
        print("Number of experiments : ", self._numExp)

class SteepestAscent(HillClimbing):
    def run(self, p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC: # 후보값이 현재보다 크거나 같으면 
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)
    
    def bestOf(self, neighbors, p): 
        best = neighbors[0]     # 'best' is value lis
        bestValue = p.evaluate(best)

        for i in range(1, len(neighbors)):
            newValue = p.evaluate(neighbors[i])
            if newValue < bestValue: # 좋은거. 새로운 값을 찾은거
                best = neighbors[i]
                bestValue = newValue
        return best, bestValue
    
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        HillClimbing.displaySetting(self)
    

class FirstChoice(HillClimbing):
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        HillClimbing.displaySetting(self)
        print("Max evaluations with no improvement: {0:,} iterations"
          .format(self._limitStuck))

class GradientDescent(HillClimbing):
    def run(self, p):
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
        p.storeResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: Gradient-descent Hill Climbing")
        print()
        print("Update size:", self._alpha)
        print("Increment for calculating derivatives : ", self._dx)