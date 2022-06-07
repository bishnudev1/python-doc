
# Getter and Setter Method in Encapsulation

class Student:

    def __init__(self):
        self.name = ''
    
    def getName(self):
        return self.name
    
    def setName(self,myName):
        self.name = myName


Name = Student()
Name.setName('Bishnudev Khutia')
print(Name.getName())