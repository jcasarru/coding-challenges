'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
import datetime

now = datetime.date.today().year

name = input('Which is your name? ')
age = input('Which is your age? ')
random = input('Enter a random number: ')

# print(f'Hi {name}, by {now+(100-int(age))} you will have 100 years!')

print(f'Hi {name}, by {now+(100-int(age))} you will have 100 years!\n'*int(random))