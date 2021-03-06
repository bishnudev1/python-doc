# python-doc
Basic to Advanced Python Resources

## What is Python ?
Python is an interpreted,object-oriented,high-level programming language with dynamic semantics.
Python syntax are easy compared to other languages.

## What are the features of Python ?
- Open source and easy to learn
- Broad standard library
- Cross Platform
- Work on Interpreter Logic
- Multi-Paradigm Language
- High level programming
- Extendable Language
- Expressive Programming Language
- GUI Support

## What are the application of Python ?
- Network Programming
- Data Analysis
- Robotics
- Website & Application Development
- Desktop Application
- Games Development
- Web Scraping
- Data Visualization
- Scientific Calculation 
- Machine Learning & AI
- 3D Application Development
- Audios & Videos Software Development

## Creating Our First Python Program
```bash
print('Hello,World!)
```
## What are the rules of declaring variables ?
- Variable names are not Case-Sensitive
- There should be no space in Variable names
- Variables addreas are depend on it's size not it's type like other languages
```bash
a = 10
b = 20.5
c = False
print(a,b,c)
```
Taking Input/Data from User
```bash
a = input('Enter your name : ')

b = int(input('Enter first number : '))
c = float(input('Enter second number : '))
```
Printing The User-Input Data
```bash
print(f"Your name is : {a}")
print(c+b)
```
## Data Types in Python
 There is two types of datatypes in Python

- Mutable [ Can change it's state or contents ]
--- List, Dictionary, Byte array

- Immutable [ Can't change it's state or contents ]
--- Int,Float,Complex,String,Tuple,Set

1. Number
   - Integars [ 2,3,4,5,29 ]
   - Floating Point [2.5,3.4,9.1 ]
   - Complex Number [ 1+2i, 9+3j ]
```bash
a = 20
b = 10.5
c = 1 + 2j

print(type(a))
print(type(b))
print(type(c))
```
2. String
   - 'Hello'
   - "This is awesome@123"
   - 'This is also a string'
   - '''
	My name is
		Bishnudev
			Khutia
     '''
```bash
a = "Hello,World!"
b = 'Hello,World!'
c = '''
    Hello,
    World!
'''

print(a)
print(b)
print(c)
```
3. List
   - List is an ordered sequence of items and it's the most used datatypes of python.
   - example of List is l = [2,3.5,"Bishnudev"]
```bash
l = [2,8.4,"Bishnudev",False]


for item in l: 
    print(item)
    
print(type(l))
```
4. Tuple
   - Tuple is faster List but you can't modify items in it
   - example of Tuple is t = (2,4.5,'Hello')
```bash
t = (10,20,'Hello')

print(type(t))
```
5. Dictionary
   - It contains Key and Value in it
   - It mutable data type, you can modify items in it
   - It mostly use in Database works
   - example of Dictionary is dic = {
    'name':"Bishnudev",
    'age':20,
    'isSmoking':False
}
```bash
dic = {
    'name':"Bishnudev",
    'age':20,
    'isSmoking':False
}

print(dic['name'])
print(dic)
```
6. Set
   - You can't repeat same items in it
   - It's a immutable datatype just like Tuple
   - example of Set is s = {2,3,"Hi",True}
```bash
s = {10,20,30,40,10}

print(s)
print(type(s))
```
## Conditional Statements
- If Statements
```bash
age = 10

if(age >= 18):
    print('Hey, you can watch this movie')
```
- If-Elif Statements
```bash
age = 10

if(age >= 18):
    print('Hey, you can watch this movie')
elif(age > 8):
    print('Warning, watch this movie at your own risk')
```
- If-Else Statements
```bash
age = 10

if(age >= 18):
    print('Hey, you can watch this movie')
elif(age > 8):
    print('Warning, watch this movie at your own risk')
else:
    print("You can't watch this move")
```
## Operators
- Arithmetic Operators in Python
```bash
a = 20
b = 10
```
1. Addtion (+)
```bash
print(a+b)
```
2. Subtraction (-)
```bash
print(a-b)
```
3. Multiplication (*)
```bash
print(a*b)
```
4. Division (/)
```bash
print(a/b)
```
5. Modulus (%)
```bash
print(a%b)
```
6. Exponents (**)
```bash
print(a**b)
```
7. Floor Division (//)
```bash
print(a//b)
```

## Assignment Operators in Python
```bash
x = 10
```
1. Increment Operator (+=)
```bash
x += 4
print(x)
```
3. Decrement Operator (-=)
```bash
x -= 4
print(x)
```
4. Equal Operator (==)
```bash
x == 12
print(x)
```
## Bitwise Operators in Python
```bash
x = 10
y = 8

print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)
print(bin(x^y),x^y)
```
### Comparison Operator in Python

```bash
a = 25
b = 15
c = 25
```

1. Greater than (>)
```bash
print(a > b)
```
2. Less than (<)
```bash
print(a < b)
```
3. Less than equalto (<=)
```bash
print(a <= b)
```
4. Greater than equalto (>=)
```bash
print(a >= b)
```
5. Equalto (==)
```bash
print(a == b)
```
6. Not equalto (!=)
```bash
print(a != b)
```
### Identify Operators in Python

```bash
a = 10
b = 10.5
c = 'Hello,World!'
```

1. is -> Returns True if both variables are the same object
```bash
print(a is b)
```
2. is not -> Returns True if both variables are not the same object
The difference between Comparision and Identify Operators is that Identify Operator check the datatypes of two variables where Comparision Operator checks the Value of the variables
```bash
print(a is not b)
print(c is not a)
```

### Logical Operators in Python
```bash
x = 10
y = 10.5
z = 5
```
1. Union (and)
```bash
print(x > y and z == y)
```
2. Or (or)
```bash
print(x > y or z == y)
```
3. Not (not)
```bash
print(not x > y)
```

### Membership Operators in Python
myName = 'Bishnudev'
l = [10,20,30,40,50]

1. in -> Return True value if a string contains a word.
```bash
print('b' in myName)
print('B' in myName)
print('n' in myName)
```
2. not in -> Return False value if a string does not contain a word.
```bash
print(60 not in l)
print(20 in l)
```

## Loops
While Loops in Python
- The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
- We generally use this loop when we don't know the number of times to iterate beforehand.
Syntax of while Loop in Python
while test_expression:
    Body of while
```bash
i = 1

while(i != 11):
    print(i)
    i += 1
```
```bash
n = 10

while n >= 1:
    print('This is awesome')
    n -= 1

print(n)
```
For Loops in Python
- The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
- We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

Syntax of for Loop
for val in sequence:
    loop body
```bash
for i in range(1,11):
    print(i)
```
```bash
for n in range(10,0,-1):
    print(n)
```
## String Functions & Operations

### String Concatinations
- Only same datatypes can concat with each other
- Two different datatypes will give error such like a String & a Integar can't join
```bash
a = 'Hello'
b = 'World'
c = a + ' ' + b

print(c)
```
```bash
x = 10
y = 25
z = x + y

print(z)
```
Error
```bash
p = 'This is a string'
q = 30
r = p + q

print(r)
```
### String Indexing in Python
- It starts from 0 to len(str)

```bash
str = 'My name is Bishnudev Khutia'

print(str[4])
print(str[2])
print(str[12])
print(str[-5])
```
### String Iteration in Python
```bash
str = "This is a String data type"

t = len(str)
```
```bash
for a in range(t):
    print(str[a])
```
- Printing a String in Reverse(Method 1)
```bash
str = str[-1::-1]

for a in range(t):
    print(str[a])
```
- Printing a String in reverse (Method 2)
```bash
for a in range(t,-1,-1):
    print(str[a])
```
- Printing a String without it's length
```bash
for a in str:
    print(a)
```
### String Slicing in Python
- It contents three values 1. Start Index 2. End Index 3. Slice Value
```bash
str = 'My name is Bishnudev Khutia'
```
- Upper syntax means It starts from 0 index and continue still the end of the string without slicing
```bash
print(str[0:len(str)])
```
- Upper syntax remains same like upper just it will slice every one word after one word
```bash
print(str[0:len(str):2])
```
- Upper syntax reverse the string
```bash
print(str[-1::-1])
```
### String Most Used Functions
```bash
str = "Hello World !"
```
- Lower Function -> Convert the string into small letters
```bash
print(str.lower())
```
- Higher Function -> Convert the string into big letters
```bash
print(str.upper())
```
- Capitalize Function -> Captilize all characters in a string
```bash
print(str.capitalize())
```
- Title Function -> Format a string like Title names
```bash
print(str.title())
```
- Find Function -> Returns index value of a characters if it is present in a string
```bash
print(str.find('e'))
```
- Index Function -> Returns the index of a characters
```bash
print(str.index('W'))
```
- isAlpha Function -> Returns Boolean value if a String is alpha or not
```bash
print(str.isalpha())
```
- isdigit Function -> Returns Boolean value if a String is digit or not
```bash
print(str.isdigit())
```
- isalnum Function -> Returns Boolean value if a String is alnum or not
```bash
print(str.isalnum())
```
- chr Funtion - > Convert an Integer to it's matching ASCII Character
```bash
print(chr(66))
```
- ord Funtion - > Convert a ASCII Character to it's matching Integer Value (Only takes one letter from left to right)
```bash
print(ord('B'))
```
- Format Function -> Used to format a data(vale) and insert in between Strings in runtime
```bash
str2 = "Hii my name is {Name}".format(Name="Bishnudev Khutia")
print(str2)
```
```bash
str3 = "My favourite number is {Num} because it's {Name}'s birthday date".format(Num=20,Name="Bishnudev")
print(str3)
```
```bash
str4 = "Hello everyone hope everyone is {0} otherwise it's {1}".format("fine","Lol")
print(str4)
```
```bash
str5 = "Welcome {} to {}".format("Bishnudev","India")
print(str5)
```
## List Functions & Operations

### Iterations of List
```bash
L = [2,4,6,8,"Bishnudev",False,["One","Two",3,5]]
```
- Method 1
```bash
l = len(L)

for a in range(l):
    print(L[a])
```
- Method 2
```bash
for item in L:
    print(item)
```
### Slice of a List

```bash
L = [2,3,4,8,9,"Hello"]
```
```bash
print(L[0:2])

print(L[0::2])

print(L[3:])
```
- Reverse a List by Slicing
```bash
print(L[-1::-1])
```
### Index of a List

```bash
L = [2,3,4,8,9,"Hello"]
```
```bash
print(L[3],L[1])

print(L[-1])
```
### How to Create a new List containing 1 to 100 numbers ?

```bash
L = []

for i in range(1,101):
    L.append(i)
```
```bash
print(L)
```
### Functions in List
```bash
l = [2,8.4,"Bishnudev",False]
```
- Delete methods in a List
```bash
del(l[2])
```
```bash
l.pop(2)
```
```bash
l.remove(2)
```
```bash
l.clear()
```
- Update methods in a List
```bash
l = [2,8.4,"Bishnudev",False,2]
```
```bash
l[0] = 9
```
```bash
l.insert(3,"UI Goku")
```
```bash
l.append("UE Vegeta")
```
```bash
n = {2,3,4}
l.extend(n)
```
```bash
print(l.count(2))
```
```bash
L = [9,4,5,1,2]

print(max(L))
```
```bash
print(min(L))
```
```bash
L.sort()
```
```bash
L.reverse()
```
```bash
print(L.index(1))
```
- Zip -> Used to iterate two List at the same time
```bash
l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]

for a,b in zip(l1,l2):
    print(a,b)
```
### How to Convert a String into a List ?
- Method 1
```bash
str = input("Enter the value : ")

l = str.split()
```
- Method 2
```bash
m = [str]
```
- Method 3
```bash
L = []

for a in range(1,4):
    k = input(f"Enter the value of {a} : ")
    L.append(k)
```
## Tuple Functions & Operations

### Iterations of Tuple
```bash
t = (10,20,30,'Tuple','Immutable')
```
- Method 1
```bash
l = len(t)

for a in range(l):
    print(t[a])
```
```bash
for items in t:
    print(items)
```
```bash
T = (10,20,30,40,50,10,10)
```
```bash
print(min(T))
```
```bash
print(max(T))
```
```bash
print(T.count(10))
```
```bash
print(T.index(40))
```
```bash
print(sum(T))
```

## Dictionary Functions & Operations

```bash
d = {
    'course':'Python',
    'duration':'3 Months',
    'source':'Github'
}
```
- get() Function -> Returns the value according the keys
```bash
print(d.get('duration'))
```
- keys() Function -> Get the keys of a dictionary
```bash
print(d.keys())
```
- Values() Function -> Get the values of a dictionary
```bash
print(d.values())
```
- items() Function -> Get all the items (Keys + Values)
```bash
print(d.items())
```
- Deletion Functions in Dictionary
```bash
d.pop('source')
```
```bash
del d ['duration']
```
- Update method
```bash
d.update({
    'course':'Django'
})
```
- Clear method -> Clear whole Dictionary
```bash
d.clear()
```
- Insert method
```bash
d['desc'] = 'This is a Python tutorial'
```
- dict method -> Creating a Dictionary
```bash
D = dict(name='Bishnudev',hobby='Coding')
```
### Nested Dictionary
```bash
d = {
    'name' : {
        'mainName' : 'Bishnudev',
        'surName' : 'Khutia'
    },
    'roll' : {
        'collegeRoll' : 'CSE/20/020',
        'univerRoll' : 1070120026
    }
}
```
- Print a value
```bash
print(d['roll']['univerRoll'])
```
- Iterate the nested dictionary
```bash
for k,v in d.items():
    print(k,v['surName'])
```
## Set Functions & Operators

### Iteration in Sets

```bash
s = {10,20,30,'Sets','Unorder','Unindex'}
```
```
for items in s:
    print(items)
```
### Convert List into a Set

```bash
l = ['Hello','Hi','Greetings','Hola','Hay']
print(set(l))
```
```bash
S.add(80)
```
```bash
S.pop()
```
```bash
S.remove(30)
```
```bash
S.clear()
```
```bash
S.discard(20)
```
- Update Function -> Creates a new Sets from a old Set
```bash
new_s = [10,20,30,120]

S.update(new_s)
```
## Modules in Python
There's two types of Module
- Inbuilt Module
- User-Defined Module
- We need to import it in our Python program to use it
- It can be Class, Funtion or just some bunch of codes that we can use it in our other program
### First Program
```bash
def hello(name):
    return f'Hello {name}'
```
### Use it in Second Program
```bash
from Module import hello

print(hello('Bishnudev'))
```
### Math Module
```bash
import math
```
- CEIL -> Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x__ceil__(), which should return an Integral value.
```bash
x = 10.6
print(math.ceil(x))
```
- FABS -> Return the absolute(positive) value of x
```bash
x = -10
print(math.fabs(x))
```
- Factorial -> Return the factorial value of x
```bash
x = 6
print(math.factorial(x))
```
- Floor -> Opposite of CEIL Function
```bash
x = 13.3
print(math.floor(x))
```
- FSUM(Iterable) -> Return the sum of a List,Tuple
```bash
l = [3,9,2,1,12]
print(math.fsum(l))
```
- SQRT -> Returns the square root value of x
```bash
x = 81
print(math.sqrt(x))
```
### Random Module
```bash
import random
```
- Randint -> Generates a random between two range
```bash
print(random.randint(1,9))
```
- Randrange -> Generates two random between except last range number
```bash
print(random.randrange(2,4))
```
- Random Choice -> Generate a random number in a list
```bash
l = [1,2,3,4,5,6]

print(random.choice(l))
```
- Random -> Generate a float number 
```bash
print(random.random())
```
- Shuffle -> Shuffle the list 
```bash
random.shuffle(l)
print(l)
```
- Uniform -> Generates a random float value between range
```bash
print(random.uniform(1,5))
```
### Datetime Module
```bash
import datetime
```
- How to get all date & time with one line of code ?
```bash
print(datetime.datetime.now()) 
```
- Creating Date Objects
```bash
print(datetime.datetime(2022,2,2))
```
### Pickle Module
- Pickle modules helps us to create and load python data in it
- We can store List, Tuple or any object to a txt or other file
- Write Data with Pickle
```bash
l = [10,20,30,40,50,60,70,80,90,100]

file = open('writeData.txt','wb')

pickle.dump(l,file)

file.close()
```
- Read Data with Pickle
```bash
file = open('writeData.txt','rb')

l = pickle.load(file)
print(l)
```
## JSON in Python

- JSON (Javascript Object Notation).
- It is mainly used for storing and transferring data between the browser and the server.
- JSON is text,written with Javascript Object Notation.
- Python too supports JSON with a built-in-package called json
```bash
import json
```
### JSON supports mainly 6 data types 
- String
- Number
- Boolean
- Null
- Object
- Array
- In Python JSON exists as a string.
```bash
p = '{"name:"Bishnu","lang":["Python","Java"]}'
```
### Creating JSON file in Python !
```bash
import json
```
```bash
d = {
    'course':'JSON',
    'fees':2000,
    'duration':'1 Month'
}
```
```bash
f = json.dumps(d)
```
```bash
print(f)
```
### Convert JSON to Python Object !
- You can parse a JSON to Dictionary by using json.loads() method.
```bash
x = '{"course": "JSON", "fees": 2000, "duration": "1 Month"}'
```
```bash
y = json.loads(x)
print(y)
```
### Writing & Reading JSON File (File-Handling)
- Suppose you have a JSON API called posts.json
- You can get this api data easily by file handling method in python
```bash
import json

file = open('posts.json','r')
x = file.read()

finaldata = json.loads(x)
```
- Iterate the data by loop
```bash
for a in finaldata:
    print(a['title'],a['userID'])
```
## Object Oriented Programming in Python

### Class & Object
- Python is an object oriented programming language.
- Almost everything in Python is an object, with its properties and methods.
- A Class is like an object constructor, or a "blueprint" for creating objects.
- Create a Class
```bash
class DemoClass:
	a = 20
```
- Create a Object
```bash
myobj = DemoClass()
```
- Get the value of a
```bash
print(myobj.a)
```
### Methods & Constructor
- Create a Method in a Class
```bash
class Hello:
	def Sum(self):
		print(20+30)
```
- Call the sum Method
```bash
myobj1 = Hello()
myobj1.Sum()
```
### Use of self keyword in Method
- We use self keyword in Methods in a Class
- Without using self tag you can't access a local variable even it's declared in a Class
- You can use multiple arguments in a Method but self is mandetory otherwise it's just act like a Function not like a Method
```bash

class LearnSelf:
    a = 15

    def getValue(self):
        print(self.a)

    def greet(self):
        print('Hello Everyone !')

    def addtion(self,x):
        print(self.a + x)

myObj = LearnSelf()

myObj.getValue()
myObj.greet()
myObj.addtion(22)
```
```bash
class LearnSelf:
        def addtion(self,x,y):
            print(x + y)
    
myObj = LearnSelf()
myObj.addtion(22,78)
```

### Constructor in Python
- Constructors are nothing but Methods where we don't need to Call them.
- They will call itself while we make our Objects
- Syntax of Constructor : __init__
```bash
class Constructor:
    def __init__(self):
        print('This is a Constructor !')

newObj = Constructor()
```
### Inheritance in Python
- We can make a new Class from an another Class
- We can call any Method from old/another Class by New Classes Object
- There's 3 inheritance in Python
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance

Single Inheritance
- Make a class A
```bash
class A:
    def displayA(self):
        print('This is Display A')
```
- Make a class B with A
```bash
class B(A):
    def displayB(self):
        print('This is Display B')
```
- Make a object of class B
```bash
ObjectB = B()
```
- Get the value of A class and B class with B classes object
```bash
ObjectB.displayA()
ObjectB.displayB()
```
Multilevel Inheritance
- Just like Single Inheritance but we can make more than 3 Class here
```bash
class A:
    def displayA(self):
        print('This is Display A')
```
```bash
class B(A):
    def displayB(self):
        print('This is Display B')
```
```bash
class C(B):
    def DisplayC(self):
        print('This is Display C')
```
```bash
ObjectC = C()
```
```bash
ObjectC.displayA()
ObjectC.displayB()
ObjectC.DisplayC()
```
Multiple Inheritance
- We can make One new Class from two Defined Class
```bash
class A:
    def displayA(self):
        print('This is Display A')
```
```bash
class B:
    def displayB(self):
        print('This is Display B')
```
```bash
class C(A,B):
    def displayC(self):
        print('This is Display C')
```
```bash
ObjectC = C()
```
```bash
ObjectC.displayA()
ObjectC.displayB()
ObjectC.displayC()
```
## Encapsulation in Python
An object variables should not always be directly accessible.
The methods can ensure the correct values are set. If an incorrect value is set, the method can return an error.
There's two Function
- Getter Function -> Return the setting data with Constructor
- Setter Function -> Set the data via Constructor
```bash
class Student:

    def __init__(self):
        self.name = ''
    
    def getName(self):
        return self.name
    
    def setName(self,myName):
        self.name = myName
```
```bash
Name = Student()
Name.setName('Bishnudev Khutia')
print(Name.getName())
```
## Polymorphism in Python
It means same function name (but different signatures) being uses for different types.
There's two type of Polymorphism
### Overloading
- We don't need to pass Parameter in Overloading Function (Not Mandetory)
```bash
class Overloading:
    def display(self,name=''):
        print('Hello '+name)
```
```bash
obj = Overloading()
obj.display()
obj.display('Bishnudev')
```
### Overridding
- We can overwrite a same named function in two different class with Inheritance
```bash
class Class1:
    def display(self):
        print('This is Display 1')

class Class2(Class1):
    def display(self):
        # Now if we want to run display from Parent Class / Class 1 we have to use super() keyword
        super().display()
        print('This is Display 2')
```
```bash
obj = Class2()
obj.display()
```
## Errors and Built-in Exceptions
These errors can be broadly classified into two classes
- Syntax Errors ( Can't be handled, You have to fix them in your own )
```bash
a = 10
b = 20

if a == b
    print('Equal')
else
    print('Not Equal')
```
- Logical Errors ( Exceptions )
```bash
print(1/0)
```
```bash
l = [10,20,30,40,50]
print(l[6])
```
### Exception Handling
Errors we can handle or fix with program are called Exception Handling
- ZeroDivisionError
```bash
a = 10
print(1/0)
```
- NumError
```bash
print(b)
# b is not defined
```
- TypeError
```bash
a = 10
b = 'Hello'
print(a+b)
```
- ValueError
```bash
a = int(input('Enter the no : ')
# If you give input 'Hello' or string instead of 10 or any number it gives error
```
- IndexError
```bash
l = [10,20,30,40,50]
print(l[6])
```
- KeyError
```bash
d = {'name':'Bishnudev','id':'101'
print(d['roll'])
```
- ModuleNotFoundError
```bash
print(random.randint[0,10])
```
- ImportError
If any functions are not available in imported module then it wil give error

## SQLite Database with Python
Coming Soon :)
