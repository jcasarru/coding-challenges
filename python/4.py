'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

from math import floor

random = input('Enter a random number: ')

p_divisors = [x for x in range(1,floor(int(random)/2)+1)]

divisors = [x for x in p_divisors if int(random)%x == 0]

divisors.append(int(random))

print(divisors)
