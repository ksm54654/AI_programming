class HUMAN:
    SECRETNUMBER = 486
    def __init__(self, num):
        self._num = num

    @classmethod
    def do_something(cls):
        cls.SECRETNUMBER += 1

h1 = HUMAN(10)
h2 = HUMAN(10)

h1.do_something()

print(h1.SECRETNUMBER)
print(h2.SECRETNUMBER)

# print(h1._num)
# print(h2._num)

# print(h1.SECRETNUMBER)
# print(h2.SECRETNUMBER)

# h1._num += 1
# h2._num += 1

# print(h1._num)
# print(h2._num)

print(h1.SECRETNUMBER)
HUMAN.SECRETNUMBER += 1
print(h2.SECRETNUMBER)
        