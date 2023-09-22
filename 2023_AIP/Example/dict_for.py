d = {
    'Park':12345,
    'Kim':234234,
    'Lee':239084023
}

# for key, value in d.items():
#     print('{}: {}'.format(key, value))

for v in d.values():
    # key = v[0]
    # value = v[1]
    print(v)

for i, (key, value) in enumerate(d.items()): # .items를 붙여야 key의 value값도 같이 나옴!!! 
# for i, key, value in enumerate(d.items()):
    print('{}번째 : {} - {}'.format(i, key, value))




# 튜플
# a, b, c = (1, 2, 3)