

class A:
    def displayA(self):
        print('This is Display A')

class B(A):
    def displayB(self):
        print('This is Display B')

class C(B):
    def DisplayC(self):
        print('This is Display C')

ObjectC = C()

ObjectC.displayA()
ObjectC.displayB()
ObjectC.DisplayC()