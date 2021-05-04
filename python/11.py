'''
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
'''

from math import floor

def get_integer(help_text="Input a number: "):
    return int(input(help_text))


def get_divisors(number):
    p_divisors = [x for x in range(1,floor(number/2)+1)]
    divisors = [x for x in p_divisors if number%x == 0]
    return divisors


if __name__ == "__main__":
    number = get_integer()
    divisors = get_divisors(number)

    if len(divisors) > 2:
        print("Not a prime number")
    else:
        print("You found a prime number")