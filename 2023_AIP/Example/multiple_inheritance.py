class A:
    def print():
        print('I am A')

class B():
    def print():
        print('I am B')

class C(A, B):
    pass

class D(B, A):
    pass

class E(B, A):
    def print():
        print('I am E')

class F:
    def print():
        print('I am F')

class G():
    def print():
        print('I am G')

class H(F, G):
    pass

class I(E):
    pass

class J(H, I):
    pass

class K(C, D):
    pass


A.print()
B.print()
C.print()
D.print()
E.print()