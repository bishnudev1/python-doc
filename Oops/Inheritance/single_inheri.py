

class A:
    def displayA(self):
        print('This is Display A')

class B(A):
    def displayB(self):
        print('This is Display B')

ObjectC = B()

ObjectC.displayA()
ObjectC.displayB()