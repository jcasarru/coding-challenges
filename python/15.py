'''
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 

For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
'''

import re


def get_list(help_text="Input a long string: "):
    return input(help_text)

def clean_string(string):
    return re.sub('[^\w\s]','',string)

def split_string(string):
    return string.split(' ')

def invert_list(string):
    return string[::-1]

def join_list(temp_list):
    return ' '.join(temp_list)

if __name__ == "__main__":
    string = get_list()

    print(join_list(invert_list(split_string(clean_string(string)))))
