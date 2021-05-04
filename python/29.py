'''
This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: 
Part 1, Part 2, and Part 3.

In 3 previous exercises, 
we built up a few components needed to build a Tic Tac Toe game in Python:

    Draw the Tic Tac Toe game board
    Checking whether a game board has a winner
    Handle a player move from user input

The next step is to put all these three components together to make a two-player Tic Tac Toe game! 
Your challenge in this exercise is to use the functions from those previous exercises all together 
in the same program to make a two-player game that you can play with a friend. 
There are a lot of choices you will have to make when completing this exercise, 
so you can go as far or as little as you want with it.

Here are a few things to keep in mind:

    You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
    If there are no more moves left, don’t ask for the next player’s move!

As a bonus, 
you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
'''

hbars = '---'
vbars = '|'

def check_horizontal(board, winner):
    for row in board:
        if row[0] == winner and row[1] == winner and row[2] == winner:
            return True
    return False

def check_vertical(board, winner):
    board = list(map(list, zip(*board)))
    status = check_horizontal(board, winner)
    return status

def check_diagonal(board, winner):
    if board[0][0] == winner and board[1][1] == winner and board[2][2] == winner:
        return True
    elif board[2][0] == winner and board[1][1] == winner and board[0][2] == winner:
        return True
    return False

def check_winner(board, winner):
    status = False
    status = check_horizontal(board, winner)
    if status:
        return True

    status = check_vertical(board, winner)
    if status:
        return True

    status = check_diagonal(board, winner)
    if status:
        return True

    return status

def number_to_signs(number):
    if number == 1:
        return ' X '
    elif number == 2:
        return ' O '
    else:
        return '   '

def print_board(board, size=3):  
    for x1 in range(0,size+1):
        hline = ''
        vline = ''
        for x2 in range(size+1):
            if x2 < size:
                hline += ' ' + hbars
                if x1 < size:
                    vline += vbars + number_to_signs(board[x1][x2])
            else:
                if x1 < size:
                    vline += vbars
        print(hline)
        print(vline)

def ask_for_move(player):
    help_text = f"Player {player}: select a blank (0) space "
    return input(help_text) 

def get_move(player):
    while True:
        input = ask_for_move(player)
        try:
            row = int(input[0])
            col = int(input[2])
            if row in [1,2,3] and col in [1,2,3]:
                return row, col
            else:
                print('Remember that both rows and cols range from 1 to 3, i.e., 1, 2, 3')

        except:
            print('Error: your input is not in the correct format, must be row,col; e.g. 1,1')


if __name__ == "__main__":
    _play_again = True
    player1_score = 0
    player2_score = 0

    while _play_again:
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        _continue = True
        # status = False

        print('-'*40)
        print('Start')
        print('Player 1: X')
        print('Player 2: O')
        print('You should select a blank (0) space in order to draw your selection')
        print('Your input must be as "row,col", e.g. 2,2 will draw an X/O at the center')
        while _continue:
            print("-"*20)
            print_board(game)
            if 0 not in [x for y in game for x in y]:
                _continue = False
            else:
                while True:
                    row, col = get_move(1)
                    if game[row-1][col-1] == 0:
                        game[row-1][col-1] = 1
                        break
                    else:
                        print('The space you have selected is not available, do another selection (0 or blank space)')
            
            if check_winner(game, 1):
                print('|------------------|')
                print('|                  |')
                print('|  Player 1 wins!  |')
                print('|                  |')
                print('|------------------|')
                print_board(game)
                player1_score += 1
                break
            
            print_board(game)
            if 0 not in [x for y in game for x in y]:
                _continue = False
            else:
                while True:
                    row, col = get_move(2)
                    if game[row-1][col-1] == 0:
                        game[row-1][col-1] = 2
                        break
                    else:
                        print('The space you have selected is not available, do another selection (0 or blank space)')
            
            if check_winner(game, 2):
                print('|------------------|')
                print('|                  |')
                print('|  Player 2 wins!  |')
                print('|                  |')
                print('|------------------|')
                print_board(game)
                player2_score += 1
                break

            if _continue == False:
                print('|------------------|')
                print('|                  |')
                print('|      DRAW!!!     |')
                print('|                  |')
                print('|------------------|')
        
        print('\n\n')
        print('_______SCORE________')
        print('|                  |')
        print(f'|  Player 1: {player1_score}     |')
        print('|                  |')
        print(f'|  Player 2: {player2_score}     |')
        print('|                  |')
        print('|__________________|')
        print('\n\n')

        print('If you want to play again, press enter, otherwise input exit')
        conti = input('')
        
        if conti == 'exit':
            # print(f'Your score is: {score}')
            break
        else:
            continue