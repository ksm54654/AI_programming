class Parent:
    def __init__(self):
        self._parent = 'I am a parent'
        self._temp = 'temp parent'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child = 'I am a child'
        self._

p = Parent()
c = Child()

print(p._parent)
print(c._child)
print(c._parent)