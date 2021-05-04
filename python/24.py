'''
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 

This one is 3x3 (like in tic tac toe). 
Obviously, they come in many other sizes 
(8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, 
and draw it for them to the screen using Python’s print statement.
'''

hbars = '---'
vbars = '|'

def print_board(size=3):  
    for x1 in range(0,size+1):
        hline = ''
        vline = ''
        for x2 in range(size+1):
            if x2 < size:
                hline += ' ' + hbars
            if x1 < size:
                vline += vbars + '   '
        print(hline)
        print(vline)
                
def ask_for_size(help_text="Choose the side (n) of your n x n board : "):
    return input(help_text)    

if __name__ == "__main__":
    while True:
        number = ask_for_size()
        try:
            number = int(number)
            break
        except:
            print('-'*30)
            print('Enter a valid number')

    print_board(number)