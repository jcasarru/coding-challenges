'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

random = input('Enter a random number: ')

word = "even" if int(random)%2 == 0 else "odd"

print(f'{random} is an {word} number')

# --------------------------
# Extra 1

random = input('Enter a random number: ')

word = "even" if int(random)%2 == 0 else "odd"
message = "Multiple of four" if int(random)%4 == 0 else f'{random} is an {word} number'

print(message)


# --------------------------
# Extra 2

random = input('Enter a random number: ')
random2 = input('Enter a random number: ')

word = "is" if int(random)%int(random2) == 0 else "is not"

print(f'{int(random)} {word} multiple of {int(random2)}')

