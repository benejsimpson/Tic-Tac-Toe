def clear_output():
    print('\n'*100)

def display_board(board):
    '''
    displays board
    '''
    blank_line = '   |   |   '
    print(blank_line)
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print(blank_line)
    print('-----------')
    print(blank_line)
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print(blank_line)
    print('-----------')
    print(blank_line)
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print(blank_line)

def player_input():
    '''
    accepts valid inputs for all spaces
    '''
    choice = 'WRONG'
    choice_in_range = False
    while choice.isdigit() == False or choice_in_range == False:
        choice = input('Select a position using numpad: ')

        if choice.isdigit():
            if int(choice) not in range(1,10):
                print('INVALID!')
            else:
                return int(choice)
            
def place_marker(board, marker, position):
    '''
    places X/O marker at position selected
    '''
    board[position] = marker

def win_check(board, mark):
    '''
    returns True for winning position
    '''
    r1 = [board[7], board[8], board[9]]
    r2 = [board[4], board[5], board[6]]
    r3 = [board[1], board[2], board[3]]
    c1 = [board[7], board[4], board[1]]
    c2 = [board[8], board[5], board[2]]
    c3 = [board[9], board[6], board[3]]
    d1 = [board[7], board[5], board[3]]
    d2 = [board[9], board[5], board[1]]

    lines = [r1,r2,r3,c1,c2,c3,d1,d2]

    for line in lines:
        if len(set(line)) == 1 and mark in set(line):
            print(f'Player {mark} wins!')
            return True
    return False

def choose_first():
    '''
    randomly selects X/O
    '''
    from random import randint
    
    if randint(0,1) == 0: return 'X'
    else: return 'O'

def space_check(board, position):
    '''
    returns True if space is empty
    '''
    if board[position] in ['X', 'O']:
        return False
    else:
        return True
    
def full_board_check(board):
    '''
    returns True if board is full
    '''
    for i in board[1:]:
        if i not in ['X', 'O']:
            return False
    print('Game over!')
    return True

def player_choice(board):
    '''
    returns accepted possible position
    '''
    valid = False
    while valid == False:
        choice = player_input()
        if space_check(board, choice):
            return choice
        else:
            print('ERROR: Position already occupied')
        
def replay():
    '''
    returns True to replay game
    '''
    choice = 'WRONG'
    accepted = ['Y', 'N']
    while choice not in accepted:
        choice = input('Would you like to replay? (Y/N): ').upper()
    if choice == 'Y':
        clear_output()
        return True
    return False

def setup_game():
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    turn = choose_first()
    print(f'{turn} chooses their move first!')
    return board, turn

print('Welcome to Tic Tac Toe!')
game_on = True
board, turn = setup_game()

while game_on:
    display_board(board)
    print(f'Player {turn} to make a move!')
    place_marker(board, turn, player_choice(board))
    clear_output()
    display_board(board)

    if win_check(board, turn):
        if replay():
            board, turn = setup_game()
    elif full_board_check(board):
        if replay():
            board, turn = setup_game()
    else:
        clear_output()
        if turn == 'X': turn = 'O'
        else: turn = 'X'
