

# Overloading in Polymorphism
# We don't need to pass Parameter in Overloading Function (Not Mandetory)

class Overloading:
    def display(self,name=''):
        print('Hello '+name)

obj = Overloading()
obj.display()
obj.display('Bishnudev')

# Overridding in Polymorphism
# We can overwrite a same named function in two different class with Inheritance

class Class1:
    def display(self):
        print('This is Display 1')

class Class2(Class1):
    def display(self):
        # Now if we want to run display from Parent Class / Class 1 we have to use super() keyword
        super().display()
        print('This is Display 2')

obj = Class2()
obj.display()




    