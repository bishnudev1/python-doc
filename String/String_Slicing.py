str = 'My name is Bishnudev Khutia'

# String slicing in Python
# It contents three values 1. Start Index 2. End Index 3. Slice Value

print(str[0:len(str)])
# Upper syntax means It starts from 0 index and continue still the end of the string without slicing

print(str[0:len(str):2])
# Upper syntax remains same like upper just it will slice every one word after one word

print(str[-1::-1])
# Upper syntax reverse the string