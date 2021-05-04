'''
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, 
not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space, 
and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, 
tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
'''


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

 
if __name__ == "__main__":
    print('-'*40)
    print('Example 1')
    board = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 1]]
    
    print(board)

    player_1 = check_winner(board, 1)
    player_2 = check_winner(board, 2)

    print(f'Player 1 wins: {player_1}')
    print(f'Player 2 wins: {player_2}')

    print('-'*40)
    print('Example 2')
    board = [[1, 2, 2],
             [1, 2, 0],
             [2, 1, 1]]
    
    print(board)

    player_1 = check_winner(board, 1)
    player_2 = check_winner(board, 2)

    print(f'Player 1 wins: {player_1}')
    print(f'Player 2 wins: {player_2}')

    print('-'*40)
    print('Example 3')
    board = [[1, 1, 0],
             [2, 1, 0],
             [2, 1, 2]]
    
    print(board)

    player_1 = check_winner(board, 1)
    player_2 = check_winner(board, 2)

    print(f'Player 1 wins: {player_1}')
    print(f'Player 2 wins: {player_2}')

    print('-'*40)
    print('Example 4')
    board = [[2, 1, 0],
             [2, 1, 0],
             [2, 1, 1]]
    
    print(board)

    player_1 = check_winner(board, 1)
    player_2 = check_winner(board, 2)

    print(f'Player 1 wins: {player_1}')
    print(f'Player 2 wins: {player_2}')

    print('-'*40)
    print('Example 5')
    board = [[1, 1, 1],
             [2, 1, 0],
             [2, 2, 2]]
    
    print(board)

    player_1 = check_winner(board, 1)
    player_2 = check_winner(board, 2)

    print(f'Player 1 wins: {player_1}')
    print(f'Player 2 wins: {player_2}')

