'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean.

Extras:
    Use binary search.
'''
def get_number(help_text="Input a number to be searched in a list: "):
    return input(help_text)

def validate_input():
    while True:
        option = get_number()
        try:
            return int(option)
        except:
            print('Enter a number')

def binary_search(numbers, objective):
    i = 0
    while True:
        left, right = split_list(numbers)
        i += 1
        print(f'{i} - left: {left} | right: {right} | Number: {objective}')

        if len(left) == 1 and len(right) == 1 and objective not in left and objective not in right:
            return False
        else:
            if objective == left[-1]:
                return True
            
            if objective == right[0]:
                return True

            if objective < left[-1]:
                numbers = left
            elif objective > right[0]:
                numbers = right
            else: 
                return False

def split_list(numbers):
    return numbers[0:len(numbers)//2], numbers[len(numbers)//2:]

if __name__ == "__main__":
    list_numbers = [5, 6, 7, 20, 35, 40, 50, 60, 90]
    my_number = validate_input()
    result = binary_search(list_numbers, my_number)
    print(f'Your number presence is: {result}')
    print(f'Your number: {my_number}')
    print(f'List: {list_numbers}')