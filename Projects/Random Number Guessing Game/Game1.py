
import random

def game():

    run = True

    comp = random.randint(0,50)

    while run:
        
        user = int(input("Enter your choice : "))

        if(comp == user):
            print('You guessed it right')
            run = False
        elif(comp > user):
            print('Guess higher')
        else:
            print('Guess lower')

game()
    