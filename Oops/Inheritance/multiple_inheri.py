

class A:
    def displayA(self):
        print('This is Display A')

class B:
    def displayB(self):
        print('This is Display B')

class C(A,B):
    def displayC(self):
        print('This is Display C')

ObjectC = C()

ObjectC.displayA()
ObjectC.displayB()
ObjectC.displayC()