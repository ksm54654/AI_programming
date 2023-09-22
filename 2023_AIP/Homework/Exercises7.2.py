from abc import *
import random

class Contestant(metaclass = ABCMeta):
    def __init__(self, name= ''):
        self._name = name
        self._score = 0
        self._selection = ('rock', 'scissors', 'paper')

    def getName(self):
        return self._name
    
    def getScore(self):
        return self._score
    
    def addScore(self):
        self._score += 1

    @abstractmethod
    def choose(self):
        pass

class Computer(Contestant):
    def choose(self):
        selection = random.choice(self._selection)
        print(f'{self._name} chooses {selection}')
        return selection

class Human(Contestant):
    def choose(self):
        selection = ''
        while selection not in self._selection:
            selection = input(f'{self._name}, enter your choice : ')
        return selection
        

# 둘의 선택을 입력으로 받아, 가위바위보 결과를 반환하는 기능 
'''
    choice1이 이기면, 1
    비기면, 0
    choice2가 이기면, -1
    을 반환한다.

'''
def getGameResult(choice1, choice2):
    # if(choice1=='rock' and choice2 == 'scissors')
    list_case = [('rock', 'scissors'),
                 ('scissors', 'paper'),
                 ('paper', 'rock')]
    if (choice1, choice2) in list_case:
        return 1
    elif choice1 == choice1:
        return 0
    else:
        return -1


def main():
    name_human = input('Enter name of human : ')
    name_computer = input('Enter name of computer : ')

    human = Human(name_human)
    computer = Computer(name_computer)

    for _ in range(3):
        choice1 = human.choose()
        choice2 = computer.choose()

        result = getGameResult(choice1, choice2)
        if result > 0:
            human.addScore()
        elif result < 0:
            computer.addScore()
        print(f'{human.getName()} : {human.getScore()}, \
              {computer.getName()} : {computer.getScore()}')

    if human.getScore() == computer.getScore():
        print('TIE')
    else:
        winner = human.getName()\
            if human.getScore() > computer.getScore() \
                else computer.getName()
        print(f'{winner} WINS')
    

main()