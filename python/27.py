'''
This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a “data structure” 
to store information about a tic tac toe game. 
In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, 
to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user input. 
When a player (say player 1, who is X) wants to place an X on the screen, 
they can’t just click on a terminal. 
So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. 
The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. 
Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]

And ask Player 2 for their move, printing an O in that place.

Things to note:

    For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
    Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). 
    To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. 
    This is not required, but whichever way you choose to implement this, it should be explained to the player.
    Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. 
    Then you can use your Python skills to figure out which row and column they want their piece to be in.
    Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, 
    do not allow the piece to go there.

Bonus:

    For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. 
    In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.
'''


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
    # player1, 1, X
    # player2, 2, O

    game = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    _continue = True
    status = False

    print('Start')
    print('Player 1: X')
    print('Player 2: O')
    print('You should select a blank (0) space in order to draw your selection')
    print('Your input must be as "row,col", e.g. 2,2 will draw an X/O at the center')
    while _continue:
        print("-"*40)
        print(f'{game[0][0]}{game[0][1]}{game[0][2]}\n{game[1][0]}{game[1][1]}{game[1][2]}\n{game[2][0]}{game[2][1]}{game[2][2]}')
        if 0 not in [x for y in game for x in y]:
            _continue = False
        else:
            while True:
                row, col = get_move(1)
                if game[row-1][col-1] == 0:
                    game[row-1][col-1] = 1
                    break
                else:
                    print('The space you have selected is not available, do another selection (0)')

        print("-"*40)
        print(f'{game[0][0]}{game[0][1]}{game[0][2]}\n{game[1][0]}{game[1][1]}{game[1][2]}\n{game[2][0]}{game[2][1]}{game[2][2]}')

        if 0 not in [x for y in game for x in y]:
            _continue = False
        else:
            while True:
                row, col = get_move(2)
                if game[row-1][col-1] == 0:
                    game[row-1][col-1] = 2
                    break
                else:
                    print('The space you have selected is not available, do another selection (0)')
        