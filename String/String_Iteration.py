#Printing a String by Iretation

str = "This is a String data type"

t = len(str)

for a in range(t):
    print(str[a])

#Printing a String in reverse (Method 1)

str = str[-1::-1]

for a in range(t):
    print(str[a])

#Printing a String in reverse (Method 2)

for a in range(t,-1,-1):
    print(str[a])

#Printing a String without it's length

for a in str:
    print(a)