import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

def measure(func):    # 밑에 두개 다하면 이거 해보기... 음 ㅜㅜ 
    """
        decorator function
        logging을 이용해 x값, y값, 계산값 을 출력할 수 있는 기능을 추가
    """
    def wrapper(self, *args, **kwargs):

        result = func(self, *args, **kwargs)

        # x = self._eqn[args[0]][1]
        # y = self._eqn[args[0]][2]

        logging.info(f"x값: {x}, y값: {y}, 계산값: {result}")
        return result
    return wrapper
    

class Evaluator:
    def __init__(self, filename):
        """
            filename에 주어진 경로에서 읽기 전용으로 csv 파일을 읽어서
            각 줄에 있는 수식과 변수 값을 저장

            csv 파일은 수식,x값,y값 으로 구성되어 있음

            ex) equations.txt
            10*x + 2*y,2,5
            0.5*x - 1.8*y,7,3
        """
        # open 써서 파일 열고, for문으로 줄을 읽어온다
        # split으로 csv값 구분해서 저장 
        # 리스트 이용
        self._eq = []
        file = open(filename, 'r')
        line = file.readlines()
        for line in filename:
            str = line.split(',')
            self._eq.append(str)
            
        # eqn = line.split(',')
        # eqn = [0] 수식
        # eqn = [1] 
        # eqn = [2]

    @measure
    def solve(self, idx):
        """
            idx 번째 수식을 계산한 값을 반환

            ex)
            solve(1) 은 equations.txt 의 0.5*x - 1.8*y가
            x=7, y=3일 때 값을 계산하여 반환

            solve 내부에는 logging이나 print 사용하지 말 것
        """
        # exec 또는 eval을 잘 쓰면 됨. 
    
        eqn = self._eq[idx]
        result = eval(eqn[0])

        x = float(eqn[1])
        y = float(eqn[1])

        

        return result
        # exec('x=' +eqn[1])
        # exec('y=' +eqn[2])
        # eval(eqn[0])

    
def main():
    evaluator = Evaluator('equations.txt')
    assert np.allclose(evaluator.solve(0), 30)
    assert np.allclose(evaluator.solve(1), -1.9)

main()
