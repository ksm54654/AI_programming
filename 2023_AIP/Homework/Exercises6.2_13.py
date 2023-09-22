import random

cnt = 0

for _ in range(100):
    #print(_) # _는 변수다 
    #if random.choice(['H', 'T']) == 'H':
    if random.random() > 0.5: # 0.5보다 크면 앞면 
        cnt += 1

print('Heads: {}'.format(cnt))