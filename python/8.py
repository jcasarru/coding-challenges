'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''
def get_selection():
    # print('Choose an option\n')
    print("1: 'rock', 2: 'paper', 3: 'scissors'")
    selection = input('Enter your number: ')
    return selection

def validate_selection():
    while True:
        option = get_selection()
        if int(option) not in [1, 2, 3]:
            print('Enter a valid option (1, 2 or 3)')
        else:
            return option
def turns(p1, p2):
    print(f'\n{p1} 1 turns')
    option1 = int(validate_selection())
    print(f'\n{p2} 1 turns')
    option2 = int(validate_selection())

    return option1, option2

def get_winner(op1, op2, player1, player2):
    # 1: 'rock', 2: 'paper', 3: 'scissors'
    if op1 == 1 and op2 == 2:
        winner = player2
    elif op1 == 1 and op2 == 3:
        winner = player1
    elif op1 == 2 and op2 == 1:
        winner = player1
    elif op1 == 2 and op2 == 3:
        winner = player2

    return winner


if __name__ == "__main__":
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    player1 = input('Player 1 names: ')
    player2 = input('Player 2 names: ')
    while True:
        op1, op2 = turns(player1, player2)
        if op1 == op2:
            print('*'*50)
            print('There is no winner')
            print('*'*50)
            continue
        else:
            winner = get_winner(op1, op2, player1, player2)
            print('*'*50)
            # print('somebody has won')
            print(f'{winner} has won!')
            print('*'*50)
            break

