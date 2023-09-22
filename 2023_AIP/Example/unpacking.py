# 언패킹
def print_num(a, b, c):
    print(a)
    print(b)
    print(c)

nums = [10, 20, 30]

print_num(*nums)

# 가변인수
def print_numbers(*args):
     for arg in args:
         print(arg)

print_numbers(*(1, 2, 3, 4, 5))

# 키워드 인수
def personal_info(name, age, address):
    print(name)
    print(age)
    print(address)

data = {'name' : 'JS', 'age' : 10, 'address' : 'Busan' }

personal_info(name=data['name'],
              age=data['age'],
              address=data['address'])

personal_info(**data)
personal_info(*data)

# 키워드 가변인수
def personal_info2(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} : {v}')

data2 = {'name' : 'JS', 'address' : 'Busan' }

personal_info2(**data)
personal_info2(**data2)
