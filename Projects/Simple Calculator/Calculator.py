print(''' Sum : + || Subs : - || Multi : * || Div : / ''')
a = float(input('Enter number 1 : '))
b = float(input('Enter number 2 : '))

while True:
    c = input('Enter Operation : ')

    if(c == '+'):
        print(a+b)
    elif(c == '-'):
        print(a-b)
    elif(c == '*'):
        print(a*c)
    elif(c == '/'):
        print(a/b)
    else:
        print('Wrong Operation Chosen !')