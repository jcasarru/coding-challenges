'''
This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, 
but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman, 
the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. 
In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

    Only let the user guess 6 times, and tell the user how many guesses they have left.
    Keep track of the letters the user guessed. 
    If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

Optional additions:

    When the player wins or loses, let them start a new game.
    Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. 
    This is challenging - do the other parts of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!
'''

# To Do: make use of sets instead of lists
# To Do: Draw hangman

import random


def read_lines_to_list(fullfilepath):
    content = []
    with open(fullfilepath, 'r') as o_file:
        lines = o_file.readlines()
        for line in lines:
            content.append(line.strip().upper())
    return content

def ask_for_letter(guessed, target):
    while True:
        letter = input("Guess your letter: ")

        if len(letter) >= 1:
            if letter[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter[0].upper() in guessed:
                    print('You already tried with this letter!')
                else:
                    return letter[0].upper()
        else:
            print('Enter a letter, not symbols!')


if __name__ == "__main__":
    # target = 'EVAPORATE'
    words = read_lines_to_list('resources/sowpods.txt')
    _play_again = True
    
    while _play_again:
        target = random.choice(words)
        tries = 6
        total_tries = 0
        hidden_target = ['_' for _ in target]
        guessed = []
        _incomplete = True

        print('Welcome to Hangman!')
        print('Guess the word in 6 turns or less')
        print(' '.join(hidden_target))

        while _incomplete:
            print('\n')
            letter = ask_for_letter(guessed, target)
            guessed.append(letter)
            total_tries += 1

            if letter in target:
                for i, symbol in enumerate(target):
                    if symbol == letter:
                        hidden_target[i] = letter
                print(' '.join(hidden_target))
                print(f'{tries} remaining')
            else:
                print('Sorry, your selected letter is not in the word!')
                tries -= 1
                print(f'{tries} remaining')

            if '_' in hidden_target:
                if tries > 0:
                    continue
                else:
                    print('You lose!')
                    print(f'Hidden word was: {target}')
                    _incomplete = False
            else:
                print(f'You get the word in {total_tries} tries')
                _incomplete = False

        
        print('If you want to play again, press enter, otherwise input exit')
        conti = input('')
        
        if conti == 'exit':
            break
        else:
            continue