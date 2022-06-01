
# String Concatination Rules
# - Only same datatypes can concat with each other
# - Two different datatypes will give error such like a String & a Integar can't join


a = 'Hello'
b = 'World'
c = a + ' ' + b

print(c)

x = 10
y = 25
z = x + y

print(z)

# Error

p = 'This is a string'
q = 30
r = p + q

print(r)