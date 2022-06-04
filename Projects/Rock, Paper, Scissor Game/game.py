
import random

def Game():
    userChoice = input('Enter your choice : ')
    rand = random.randint(0,2)
    if(rand == 0):
        compChoice = 'Rock'
    elif(rand == 1):
        compChoice = 'Paper'
    else:
        compChoice = 'Scissor'
    
    print('You chose : ',userChoice)
    print('Computer chose : ',compChoice)

    if(userChoice == 'Rock' and compChoice == 'Scissor'):
        print('You won !')
    elif(userChoice == 'Scissor' and compChoice == 'Rock'):
        print('You lost !')
    if(userChoice == 'Paper' and compChoice == 'Rock'):
        print('You won !')
    elif(userChoice == 'Rock' and compChoice == 'Paper'):
        print('You lost !')
    if(userChoice == 'Scissor' and compChoice == 'Paper'):
        print('You won !')
    elif(userChoice == 'Paper' and compChoice == 'Scissor'):
        print('You lost !')


Game()
    
