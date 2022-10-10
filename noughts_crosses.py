board = [' ' for i in range(0, 9)]


def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def user_turn(symbol, player):
    while True:
        print(f'Your turn {player}')
        choice = int(input('Pick a number (1-9): ').strip())
        if choice > 9:
            print('Sorry the number is too high.\n')
        elif choice <= 0:
            print('Sorry the number is too low.\n')
        elif board[choice - 1] == ' ':
            board[choice - 1] = symbol
            break
        else:
            print('Sorry this space is already taken.\n')


"""def winner(symbol, player):
    if symbol == board[0] and symbol == board[1] and symbol == board[2]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[3] and symbol == board[4] and symbol == board[5]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[6] and symbol == board[7] and symbol == board[8]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[0] and symbol == board[4] and symbol == board[8]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[2] and symbol == board[4] and symbol == board[6]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[0] and symbol == board[3] and symbol == board[6]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[1] and symbol == board[4] and symbol == board[7]:
        print_board()
        quit(f'{player} has won!')
    elif symbol == board[2] and symbol == board[5] and symbol == board[8]:
        print_board()
        quit(f'{player} has won!')"""


def winner(symbol):
    if (symbol == board[0] and symbol == board[1] and symbol == board[2]) or \
        (symbol == board[3] and symbol == board[4] and symbol == board[5]) or \
        (symbol == board[6] and symbol == board[7] and symbol == board[8]) or \
        (symbol == board[0] and symbol == board[4] and symbol == board[8]) or \
        (symbol == board[2] and symbol == board[4] and symbol == board[6]) or \
        (symbol == board[0] and symbol == board[3] and symbol == board[6]) or \
        (symbol == board[1] and symbol == board[4] and symbol == board[7]) or \
            (symbol == board[2] and symbol == board[5] and symbol == board[8]):
        return True
    else:
        return False


def if_draw():
    if ' ' not in board:
        return True
    else:
        return False


while True:
    print_board()
    user_turn('X', 'Player 1')
    if winner('X') is True:
        print_board()
        print('Player 1 wins!')
        break
    elif if_draw() is True:
        print_board()
        print('It is a draw...')
        break
    print_board()
    user_turn('O', 'Player 2')
    if winner('O') is True:
        print_board()
        print('Player 2 wins!')
        break
    elif if_draw() is True:
        print_board()
        print('It is a draw...')
        break
