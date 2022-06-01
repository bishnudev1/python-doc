
# Membership Operators in Python

# 1. in -> Return True value if a string contains a word.
# 1. not in -> Return False value if a string does not contain a word.

myName = 'Bishnudev'

# It will give False as Python is a Case-Sensitive Language
print('b' in myName)

print('B' in myName)
print('n' in myName)
print('j' not in myName)

l = [10,20,30,40,50]

print(20 in l)

print(60 not in l)