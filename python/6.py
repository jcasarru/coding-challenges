'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
import re

if __name__ == "__main__":
    print('Input a string and i\'ll tell you if it is a palindrome or not\n')
    phrase = input('Input phrase: ')
    
    phrase = re.sub('[^\w]','',phrase).lower()

    if phrase == phrase[::-1]:
        print('It is plalindrome')
    else:
        print('Sorry, it is not!')
