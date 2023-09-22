class Counter:
    # def __init__(self, stop):
    #     self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
    #     self.stop = stop    # 반복을 끝낼 숫자 

    # 가변인자
    def __init__(self, *args):
        if len(args) == 1:
            self._current = 0    
            self._stop = args[0]
            self._iterval = 1
        elif len(args) == 2:
            self._current = args[0]
            self._stop = args[1]
            self._iterval = 1
        elif len(args) == 3:
            self._current = args[0]
            self._stop = args[1]
            self._iterval = args[2]
        else:
            raise NotImplementedError
        
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        '''
            3의 배수일때는 "짝"이 나오게 
        '''
        if self._current < self._stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self._current            # 반환할 숫자를 변수에 저장
            self._current += self._iterval           # 현재 숫자를 1 증가시킴
            if r > 0 and r % 3 == 0:
                r = "짝"
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(5):
    print(i, end=' ')

print()
for i in Counter(2, 5):
    print(i, end=' ')

print()
for i in Counter(2, 10, 2):
    print(i, end=' ')