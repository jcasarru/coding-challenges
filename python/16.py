'''
Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. 

The passwords should be random, generating a new password every time the user asks for a new password. 

Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import string
import random
from math import floor

def generate_password(length):
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "01234567890"
    symbols = "!@#$%^&*()?"

    # plowers = 0.4
    puppers = 0.2
    pnumbers = 0.2
    psymbols = 0.2

    luppers = floor(puppers * length)
    lnumbers = floor(pnumbers * length)
    lsymbols = floor(psymbols * length)
    llowers = length - luppers - lnumbers - lsymbols

    password = ''
    password += ''.join(random.choice(lowers) for _ in range(llowers))
    password += ''.join(random.choice(uppers) for _ in range(luppers))
    password += ''.join(random.choice(numbers) for _ in range(lnumbers))
    password += ''.join(random.choice(symbols) for _ in range(lsymbols))

    return ''.join(random.sample(password, len(password)))

def get_length(help_text="Choose your password length: "):
    number = input(help_text)
    
    try:
        if int(number) >= 6:
            return int(number)
        else:
            return exit(1)
    except:
        print("Not a valid length")
        return exit(1)


if __name__ == "__main__":
    pass_size = get_length()
    print(generate_password(pass_size))