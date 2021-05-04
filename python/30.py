'''
This exercise is Part 1 of 3 of the Hangman exercise series. 
The other exercises are: Part 2 and Part 3.

In this exercise, 
the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
'''


import re
import random


def read_file(fullfilepath):
    with open(fullfilepath, 'r') as o_file:
        content = o_file.read()
    return content.split('\n')

def read_lines_to_list(fullfilepath):
    content = []
    with open(fullfilepath, 'r') as o_file:
        lines = o_file.readlines()
        for line in lines:
            content.append(line.strip().upper())
    return content


if __name__ == "__main__":
    words = read_lines_to_list('resources/sowpods.txt')
    word = random.choice(words)

    print(f'Random word: {word}')

