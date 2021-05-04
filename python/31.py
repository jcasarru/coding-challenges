'''
This exercise is Part 2 of 3 of the Hangman exercise series. 
The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, 
a clue word is given by the program that the player has to guess, letter by letter. 
The player guesses one letter at a time until the entire word has been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, 
write the logic that asks a player to guess a letter and displays letters in the 
clue word that were guessed correctly. 

For now, let the player guess an infinite number of times until they get the entire word. 
As a bonus, keep track of the letters the player guessed and display a different message 
if the player tries to guess that letter again. 

Remember to stop the game when all the letters have been guessed correctly! 
Don’t worry about choosing a word randomly or keeping track of the number of guesses 
the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...

And so on, until the player gets the word.
'''

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
    target = 'EVAPORATE'
    tries = 0
    hidden_target = ['_' for _ in target]
    guessed = []
    _incomplete = True

    print('Welcome to Hangman!')
    print(' '.join(hidden_target))

    while _incomplete:
        letter = ask_for_letter(guessed, target)
        guessed.append(letter)
        tries += 1

        if letter in target:
            for i, symbol in enumerate(target):
                if symbol == letter:
                    hidden_target[i] = letter
            print(' '.join(hidden_target))
        else:
            print('Sorry, your selected letter is not in the word!')

        if '_' in hidden_target:
            continue
        else:
            print(f'You get the word in {tries} tries')
            _incomplete = False
        





