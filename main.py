import random

def guess(x):
    # game title
    print(f"Guess the number 1-{x}!!!!")

    #cpu getting the number for the game
    correct_number = int(random.randint(1,x))

    #take in usr guess


    user_guess = 0
    # compare user guess to cpu number
    while user_guess!= correct_number:
        user_guess = int(input("What is your guess?: "))
        if user_guess > correct_number:
            print("Nope... too high Guess again!!!")
        
        if user_guess < correct_number:
            print("Nope... too low Guess again!!!")

    print("YAY you guessed it!!!!!")   




    #print(correct_number)

guess(10)    