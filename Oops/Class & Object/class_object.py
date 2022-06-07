class BasicClass:
    
    myRoll = 'CSE/20/020'
    
    def greet(self):
        name = input('Enter your name : ')
        print(f"Hello {name}, welcome to our Python tutorial !")
    
BasicObject = BasicClass()

BasicClass.greet()
print(BasicClass.myRoll)


class DemoClass:
    a = 10
    
    def sumValue(self):
        print(20+30)
        
demoobject = DemoClass()

print(demoobject.a)

demoobject.sumValue()