'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

def validate_guess():
    while True:
        option = guess()
        try:
            if int(option) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('Enter a valid option')
            else:
                return int(option)
        except:
            print('Enter a valid option')

def guess():
    return input('Make your guess: ')


if __name__ == "__main__":
    score = 0

    while True:
        objective = random.randint(1, 9)
        print('A new number has been generated')
        print('Let\'s play!!!')
        _continue = True

        while _continue:
            number = validate_guess()

            if number == objective:
                _continue = False
                score += 1
                print('You got it!!!')
            elif number < objective:
                print('too low!')
            elif number > objective:
                print('too high!')
        
        print('If you want to continue, press enter, otherwise input exit')
        conti = input('')
        
        if conti == 'exit':
            print(f'Your score is: {score}')
            exit(0)
        else:
            continue
        


