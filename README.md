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
- print(a+b)
2. Subtraction (-)
- print(a-b)
3. Multiplication (*)
- print(a*b)
4. Division (/)
- print(a/b)
5. Modulus (%)
- print(a%b)
6. Exponents (**)
- print(a**b)
7. Floor Division (//)
- print(a//b)

## Assignment Operators in Python
```bash
x = 10
```
1. Increment Operator (+=)
- x += 4
3. Decrement Operator (-=)
- x -= 3
5. Equal Operator (==)
- x == 2
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

a = 25
b = 15
c = 25

1. Greater than (>)
- print(a > b)
2. Less than (<)
- print(a > b) 
3. Less than equalto (<=)
- print(a <= b)
4. Greater than equalto (>=)
- print(a >= b)
5. Equalto (==)
- print(a == b)
6. Not equalto (!=)
- print(a != b)
### Identify Operators in Python

a = 10
b = 10.5
c = 'Hello,World!'

1. is -> Returns True if both variables are the same object
- print(a is b)
2. is not -> Returns True if both variables are not the same object
The difference between Comparision and Identify Operators is that Identify Operator check the datatypes of two variables where Comparision Operator checks the Value of the variables
- print(a is not b)
- print(c is not a)

### Logical Operators in Python
x = 10
y = 10.5
z = 5
1. Union (and)
- print(x > y and z == y)
2. Or (or)
- print(x > y or z == y)
3. Not (not)
- print(not x > y)

### Membership Operators in Python
myName = 'Bishnudev'
l = [10,20,30,40,50]

1. in -> Return True value if a string contains a word.
- print('b' in myName)
- print('B' in myName)
- print('n' in myName)
2. not in -> Return False value if a string does not contain a word.
- print(60 not in l)
- print(20 in l)
