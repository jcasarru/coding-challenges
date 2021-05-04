'''
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
But that’s not an optimal guessing strategy. 
An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. 
After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
'''

import random

def validate_guess(number):
    while True:
        option = get_feedback(number)
        if option in ['ok', 'low', 'high']:
            return option
        else:
            print('Enter appropriate feedback')
            print('ok: I guessed your number')
            print('low: your number is lower than my guessed number')
            print('high: your number is higher than my guessed number')


def get_feedback(number):
    print(f'My guess number is {number}')
    return input('Enter your feedbak (ok, low, high): ')


# def binary_search(numbers, objective):
#     i = 0
#     while True:
#         left, right = split_list(numbers)
#         i += 1
#         print(f'{i} - left: {left} | right: {right} | Number: {objective}')

#         if len(left) == 1 and len(right) == 1 and objective not in left and objective not in right:
#             return False
#         else:
#             if objective == left[-1]:
#                 return True
            
#             if objective == right[0]:
#                 return True

#             if objective < left[-1]:
#                 numbers = left
#             elif objective > right[0]:
#                 numbers = right
#             else: 
#                 return False

# def split_list(numbers):
#     return numbers[0:len(numbers)//2], numbers[len(numbers)//2:]


if __name__ == "__main__":
    # score = 0

    while True:
        max_number = 100
        numbers = list(range(max_number+1))
        print(f'Think in a number from 0 to {max_number}')
        print('Let\'s play!!!')
        _continue = True


        iters = 1
        while _continue:
            # guess = random.choice(numbers)
            # guess = ( max(numbers)//2) + random.choice(range(-max(numbers)//10, max(numbers)//10))

            guess = ( len(numbers)//2) + random.choice(range(-len(numbers)//10, len(numbers)//10))
            guess = numbers[guess]
            # if guess < min(numbers):
            #     guess = min(numbers)
            # elif guess > max(numbers):
            #     guess = max(numbers)

            feedback = validate_guess(guess)

            if feedback == 'ok':
                print('I just guessed your number!')
                print(f'I guessed your number in {iters} tries')
                break
            elif feedback == 'low':
                numbers = numbers[0:numbers.index(guess)]
            elif feedback == 'high':
                numbers = numbers[numbers.index(guess)+1:]
        
            # print('-*30')
            # print(iters, ': ', numbers)
            iters+=1
        print('If you want to continue, press enter, otherwise input exit')
        conti = input('')
        
        if conti == 'exit':
            # print(f'Your score is: {score}')
            exit(0)
        else:
            continue