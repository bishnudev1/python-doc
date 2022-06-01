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

## Variables in Python
what are the rules of declaring variables ?
- Variable names are not Case-Sensitive
- There should be no space in Variable names
- Variables addreas are depend on it's size not it's type like other languages
```bash
a = 10
b = 7.5
c = True

print(a)
print(b)
print(c)
```

## Creating Hello,World! in Python ?

```bash
print('Hello,World!')
```
## Data Types in Python
### There is two types of datatypes in Python

- Mutable [ Can change it's state or contents ]
-List, Dictionary, Byte array

- Immutable [ Can't change it's state or contents ]
-Int,Float,Complex,String,Tuple,Set

### 1. Number
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
### 2. String
   - 'Hello'
   - "This is awesome@123"
   - 'This is also a string'
   - '''
	My name is
		Bishnudev
			Khutia
     '''
```bash
print("Hello,World!)
print('Hello,Everyone!)
print(```Greetings 
         To
         All```)
```
### 3. List
- List is an ordered sequence of items and it's the most used datatypes of python.
- example of List is l = [2,3.5,"Bishnudev"]
```bash
l = [2,8.4,"Bishnudev",False]


for item in l: 
    print(item)
    
print(type(l))
```

### 4. Tuple
- Tuple is faster List but you can't modify items in it
- example of Tuple is t = (2,4.5,'Hello')
```bash
t = (10,20,'Hello')

print(type(t))
```

### 5. Dictionary
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

### 6. Set
- You can't repeat same items in it
- It's a immutable datatype just like Tuple
- example of Set is s = {2,3,"Hi",True}
```bash
s = {10,20,30,40,10}

print(s)
print(type(s))
```

## Conditional Statements in Python
### If Statement
```bash
age = 10

if(age >= 18):
    print('Hey, you can watch this movie')
```

### If-Elif Statement
```bash
age = 10

if(age >= 18):
    print('Hey, you can watch this movie')
elif(age > 8):
    print('Warning, watch this movie at your own risk')

```

### If-Else Statement
```bash
age = 10

if(age >= 18):
    print('Hey, you can watch this movie')
elif(age > 8):
    print('Warning, watch this movie at your own risk')
else:
    print("You can't watch this move")
```

## Operators in Python
### Arithmetic Operators in Python 
```bash
a = 10
b = 20
```
- Addtion (+)
```bash
print(a+b)
```
- Subtraction (-)
```bash
print(a-b)
```
- Multiplication (*)
```bash
print(a*b)
```
- Division (/)
```bash
print(a/b)
```
- Modulus (%)
```bash
print(a%b)
```
- Exponents (**)
```bash
print(a**b)
```
- Floor Division (//)
```bash
print(a//b)
```
### Assignment Operators in Python
```bash
x = 15
y = 10
```
- Increment Operator (+=)
```bash
x += 5
print(x)
```
- Decrement Operator (-=)
```bash
y -= 3
print(y)
```
- Equal Operator (==)
```bash
x == y
print(x,y)
```
### Comparison Operator in Python
```bash
a = 25
b = 15
c = 25
```
- Greater than (>)
 ```bash
 print(a > b)
 ```
- Less than (<)
 ```bash
 print(a < b)
 ```
- Less than equalto (<=)
 ```bash
 print(a <= b)
 ```
- Greater than equalto (>=)
 ```bash
 print(a >= b)
 ```
- Equalto (==)
 ```bash
 print(a == b)
 ```
- Not equalto (!=)
 ```bash
 print(a != b)
 ```
### Bitwise Operator in Python

```bash
x = 10
y = 8
```
```bash
print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)
print(bin(x^y),x^y)
```
### Identify Operators in Python
```bash
a = 10
b = 10.5
c = 'Hello,World!'
```

- is -> Returns True if both variables are the same object
```bash
print(a is b)
```
- is not -> Returns True if both variables are not the same object
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
- Union (and)
```bash
print(x > y and z == y)
```
- Or (or)
```bash
print(x > y or z == y)
```
- Not (not)
```bash
print(not x > y)
```
### Membership Operators in Python
```bash
myName = 'Bishnudev'
l = [10,20,30,40,50]
```

- in -> Return True value if a string contains a word.
```bash
print('B' in myName)
print('n' in myName)
```
- not in -> Return False value if a string does not contain a word.
```bash
print('j' not in myName)
print(60 not in l)
```
- It will give False as Python is a Case-Sensitive Language
```bash
print('b' in myName)
 ```
## Loops in Python

### While Loops in Python
- The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
- We generally use this loop when we don't know the number of times to iterate beforehand.
- Syntax of while Loop in Python
while test_expression:
   Body of while
```bash
i = 1

while(i != 11):
    print(i)
    i += 1


n = 10

while n >= 1:
    print('This is awesome')
    n -= 1

print(n)
```
### For Loop in Python
- The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
- We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).
- Syntax of for Loop
 for val in sequence:
   loop body
```bash
for i in range(1,11):
    print(i)

for n in range(10,0,-1):
    print(n)
```
## User-Input in Python

```bash
a = input('Enter your name : ')

b = int(input('Enter first number : '))
c = float(input('Enter second number : '))

print(f"Your name is : {a}")
print(c+b)
```
## String in Python
We can declare String three ways in Python
- Single Comma
```bash
print('Hello,World')
```
- Double Comma
```bash
print("Hello,World")
```
- Multi-Line 
```bash
print(``` Hello,
          World!```)
```
### String Concatination
String Concatination Rules
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
- Error
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
My name is
01 3456 89
Here 2 and 7 are count as a non word index & give Nan value just like print(str[2]) 

### String slicing in Python
- It contents three values 1. Start Index 2. End Index 3. Slice Value
```bash
print(str[0:len(str)])
```
- Upper syntax means It starts from 0 index and continue still the end of the string without slicing
```bash 
print(str[0:len(str):2])
```
```bash 
print(str[-1::-1])
```
- Upper syntax reverse the string

### Printing a String by Iteration
```bash
str = "This is a String data type"

t = len(str)

for a in range(t):
    print(str[a])
```
- Printing a String in reverse (Method 1)
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
### Functions in String
- String Functions in Python
- There's so many String functions available but some of them are actually usefull in most of the time.
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
String Type Example
```bash
str2 = "Hii my name is {Name}".format(Name="Bishnudev Khutia")
print(str2)
```
Number Type
```bash
str3 = "My favourite number is {Num} because it's {Name}'s birthday date".format(Num=20,Name="Bishnudev")
print(str3)
```
Index Type
```bash
str4 = "Hello everyone hope everyone is {0} otherwise it's {1}".format("fine","Lol")
print(str4)
```
Blank Type
```bash
str5 = "Welcome {} to {}".format("Bishnudev","India")
print(str5)
```
## List Function and Operations
- Coming Soon!
