#test board display
board = ['','x','o','x','o','x','o','x','o','x']

def display_board(board):
    print('   |   |')
    print(' '+ board[1]+' | ' +board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print(' '+ board[1]+' | ' +board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[1]+' | ' +board[2]+' | '+board[3])
    print('   |   |')

def player_1():
    marker = 'damn son'
    while not (marker =='x' or marker == 'o'):
        maker = input("player one: Do you want to be 'x' or 'o':")

        if marker == 'x':
            return ('X','O')
        elif marker == 'o':
            return ('O','X')
        else:
            continue
        break
def place_marker(board,marker,position):
    board[position] = marker




def you_win(board,marker):
    return ((board[1]== marker and board[2]== marker and board[3]== marker) or
    (board[4]== marker and board[5]== marker and board[6]== marker) or
    (board[7]== marker and board[8]== marker and board[9]== marker) or
    (board[1]== marker and board[4]== marker and board[7]== marker) or
    (board[2]== marker and board[5]== marker and board[8]== marker) or
    (board[3]== marker and board[6]== marker and board[9]== marker) or
    (board[1]== marker and board[2]== marker and board[3]== marker) or
    (board[3]== marker and board[5]== marker and board[7]== marker) or
    (board[1]== marker and board[5]== marker and board[9]== marker))
        

#player_1()
display_board(board)
you_win(board,'x')
