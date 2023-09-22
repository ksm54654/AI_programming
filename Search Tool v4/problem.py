import math 
import random
from setup import Setup

# interface
class Problem:
    def __init__(self): # 변수 정의
        Setup.__init__(self)
        self._solution = []
        self._value = 0
        self._numEval = 0

        self._bestSolution = []
        self._bestMinimum = 0.0
        self._avgMinimum = 0.0
        self._avgNumEval = 0
        self._sumofNumEval = 0

        self._pFileName = ''

    def setVariables(self, parameters):     # createProblem
        self._pFileName = parameters['pFileName']
        Setup.setVariables(self, parameters)

    def getSolution(self):
        return self._solution
    
    def getValue(self):
        return self._value
    
    def getNumEval(self):
        return self._numEval

    def randomInit(self):
        pass

    def evaluate(self): 
        pass

    def mutants(self):
        pass

    def randomMutant(self):
        pass

    def describe(self):     # describeProblem
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def storeExpResult(self, results):
        self._bestSolution = results[0]
        self._bestMinimum = results[1]
        self._avgMinimum = results[2]
        self._avgNumEval = results[3]
        self._sumOfNumEval = results[4]

    def report(self):
        print()
        print("Average number of evaluations: {0:,}".format(self._avgNumEval))


class Numeric(Problem):
    def __init__(self):
        Problem.__init__(self) ### important
        self._expression = ''
        self._domain = []

    def setVariables(self, parameters):     # createProblem
        Problem.setVariables(self, parameters)
        infile = open(self._pFileName, 'r')
        self._expression = infile.readline() # as a string
        varNames = []    # Variable names
        low = []        # lower bounds
        up = []         # Upper bounds

        line = infile.readline()
        while line != '':
            data = line.split(',')  # read from CSV
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline()

        infile.close()
        self._domain = [varNames, low, up]

    def takeStep(self, x, v):
        grad = self.gradient(x, v)
        xCopy = x[:] # 다 오차
        for i in range(len(x)):
            xCopy[i] -= self._alpha * grad[i] 
        
        if self.isLegal(xCopy):
            return xCopy
        else:
            return x

    def isLegal(self, x):
        domain = self._domain   # domain : [varNames, ]
        low, up = domain[1], domain[2]
        for i in range(len(low)):
            l, u = low[i], up[i]
            if l <= x[i] <= u:
                pass
            else:
                return False
        return True

    def gradient(self, x, v):
        grad = []
        for i in range(len(x)):
            xCopy = x[:]
            xCopy[i] += self._dx
            df = self.evaluate(xCopy) - v
            g = df / self._dx
            grad.append(g)

        return grad


    def randomInit(self): # domain: [varName, low, up]
        domain = self._domain
        low = domain[1]
        up = domain[2]
        init = []
        for i in range(len(low)):               # For each variable
            r = random.uniform(low[i], up[i])   # take a random value
            init.append(r)
        return init
 
    def evaluate(self, current):        
        self._numEval += 1
        
        expr = self._expression        # p[0] is function expression
        varNames = self._domain[0]     # p[1] is domain : [varName, low, up]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr) 

    def mutants(self, current):
        neighbors = []
        for i in range(len(current)):
            mutant = self.mutate(current, i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta)
            neighbors.append(mutant)
        return neighbors
    
    def mutate(self, current, i, d):
        curCopy = current[:]
        domain = self._domain       # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy   
    
    def randomMutant(self, current):
        i = random.randint(0, len(current)-1)
        if random.uniform(0, 1) > 0.5:
            d = self._delta
        else:
            d = -self._delta
        
        return self.mutate(current, i, d) # Return a random successor
    
    def describe(self):     # describeProblem
        print()
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):       # displayResult
        print()
        print("Average objective value: {0:,}".format(self._avgMinimum))
        print("Best solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Best minimum value: {0:,.3f}".format(self._bestMinimum))
        Problem.report(self) # super().report

    def coordinate(self):
        c = [round(value, 3) for value in self._bestSolution]
        return tuple(c)  # Convert the list to a tuple



class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

    def setVariables(self, parameters):     # createProblem
        Problem.setVariables(self, parameters)
        infile = open(self._pFileName, 'r')
        # First line is number of cities
        self._numCities = int(infile.readline())
        self._locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            self._locations.append(eval(line)) # Make a tuple and append
            line = infile.readline()
        infile.close()
        self._distanceTable = self.calcDistanceTable()

    def calcDistanceTable(self):
        table = []
        locations = self._locations
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = locations[i][0] - locations[j][0]
                dy = locations[i][1] - locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2), 1)
                row.append(d)
            table.append(row)
        return table # A symmetric matrix of pairwise distances

    def randomInit(self):   # Return a random initial tour
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init
    
    def evaluate(self, current): 
        self._numEval += 1
        n = self._numCities
        table = self._distanceTable
        cost = 0
        for i in range(n - 1):
            locFrom = current[i]
            locTo = current[i + 1]
            cost += table[locFrom][locTo]
        return cost
    
    def mutants(self, current):
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors
    
    def inversion(self, current, i, j):
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def randomMutant(self, current):     
        while True:
            i, j = sorted([random.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def describe(self):     # describeProblem
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def report(self):
        print()
        print("Average tour cost: {0:,}".format(round(self._avgMinimum)))
        print("Best of best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Best minimum tour cost: {0:,}".format(round(self._bestMinimum)))
        Problem.report(self)

    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()