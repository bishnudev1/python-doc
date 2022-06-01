# String Functions in Python
# There's so many String functions available but some of them are actually usefull in most of the time.

str = "Hello World !"

# Lower Function -> Convert the string into small letters

print(str.lower())

# Higher Function -> Convert the string into big letters

print(str.upper())

# Capitalize Function -> Captilize all characters in a string

print(str.capitalize())

# Title Function -> Format a string like Title names

print(str.title())

# Find Function -> Returns index value of a characters if it is present in a string

print(str.find('e'))

# Index Function -> Returns the index of a characters

print(str.index('W'))

# isAlpha Function -> Returns Boolean value if a String is alpha or not

print(str.isalpha())

# isdigit Function -> Returns Boolean value if a String is digit or not

print(str.isdigit())

# isalnum Function -> Returns Boolean value if a String is alnum or not

print(str.isalnum())

# chr Funtion - > Convert an Integer to it's matching ASCII Character

print(chr(66))

# ord Funtion - > Convert a ASCII Character to it's matching Integer Value (Only takes one letter from left to right)

print(ord('B'))

# Format Function -> Used to format a data(vale) and insert in between Strings in runtime

str2 = "Hii my name is {Name}".format(Name="Bishnudev Khutia")
print(str2)

str3 = "My favourite number is {Num} because it's {Name}'s birthday date".format(Num=20,Name="Bishnudev")
print(str3)

str4 = "Hello everyone hope everyone is {0} otherwise it's {1}".format("fine","Lol")
print(str4)

str5 = "Welcome {} to {}".format("Bishnudev","India")
print(str5)