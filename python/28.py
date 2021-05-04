'''
Implement a function that takes as input three variables, and returns the largest of the three. 
Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. 
All you need is some variables and if statements!
'''

def ask_for_number(number):
    help_text = f"Enter number {number}: "
    return input(help_text) 

def validate_input(number):
    while True:
        input = ask_for_number(number)
        try:
            input = float(input)
            return input
        except:
            print('Error: your input is not a number')

def get_max(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    elif n3 >= n1 and n3 >= n2:
        return n3

if __name__ == "__main__":
    number_1 = validate_input(1)
    number_2 = validate_input(2)
    number_3 = validate_input(3)

    max_number = get_max(number_1, number_2, number_3)
    print(f'{max_number} is the max of [{number_1}, {number_2}, {number_3}]')