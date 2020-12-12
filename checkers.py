'''
== Board Positions ==

 . 1 . 2 . 3 . 4
 5 . 6 . 7 . 8 .
 .10 .11 .12 .13
14 .15 .16 .17 .
 .19 .20 .21 .22
23 .24 .25 .26 .
 .28 .29 .30 .31
32 .33 .34 .35 .

== Board State Representation
 - Dictionary with keys 'x', 'o', '-'
 - Values are a list of the positions taken by each type of piece

 x . x . x . x .
 . x . x . x . x
 x . x . x . x .
 . - . - . - . -
 - . - . - . - .
 . o . o . o . o
 o . o . o . o .
 . o . o . o . o


== Moves ==
 - Moves are lists of tuples (lists because a move can have several sub-moves)
 - Each tuple will be in the form (position of the piece to move, position to move the piece to)

'''

def initial_game():
    state = {}
    state['x'] = [x for x in range(1,14) if x%9 != 0]
    state['-'] = [x for x in range(14,23) if x%9 != 0]
    state['o'] = [x for x in range(23,36) if x%9 != 0]
    return state

def game_over(state):
    for piece, taken_positions in state.items():
        if (piece in ['o', 'x']) and (len(taken_positions) == 0):
            return True
    return False

def winner(state):
    if not game_over(state):
        print('Game not over')
    else:
        for piece, taken_positions in state.items():
            if (piece in ['o', 'x']) and (len(taken_positions) != 0):
                return piece

def get_user_move():
    move = []
    submove = (0,0)
    while 1:  
        submove = input('Sub-move:')
        if submove == '':
            return move
        submove = tuple(int(x.strip()) for x in submove.split(','))
        move.append(submove)
    return move
    
def computer_play(state, piece):
    move = [(10, 15)]
    return move

def update_board(state, move, piece):
    print(move)
    for submove in move:
        print(submove)
        state = update_board_submove(state, submove, piece)
    return state

def is_valid_move(state, move, piece):
    hyp_state = state
    for submove in move:
        if is_valid_submove(hyp_state, submove, piece):
            hyp_state = update_board_submove(hyp_state, submove, piece)
        else:
            return False
    return True

def opponent_piece(piece):
    if piece =='x':
        return 'o'
    if piece == 'o':
        return 'x'


def is_valid_submove(state, submove, piece):
    # check if piece to move is actually a piece
    if submove[0] not in state[piece]:
        return False
    # check if place to move to is empty
    if submove[1] not in state['-']:
        return False
    sign = []
    if piece == 'x':
        sign.append(1)
    if piece == 'o':
        sign.append(-1)
    if 'k' in piece:
        sign = [-1, 1]
    
    for s in sign:
        if submove[1] == submove[0]+s*4  and submove[0]+s*4 %9 != 0: 
            return True
        if submove[1] == submove[0]+s*5  and submove[0]+s*5 %9 != 0: 
            return True
        if submove[1] == submove[0]+s*8 and submove[0]+s*10 %9 != 0:
            return True
        if submove[1] == submove[0]+sign*10 and submove[0]+sign*10 %9 != 0:
            return True
    return False


def get_piece_from_position(state, position):
    for piece, places in state.items():
        if position in places:
            return piece

def draw_board(state):
    nl = '\n' 
    print(f'\
     . {get_piece_from_position(state, 1)} . {get_piece_from_position(state, 2)} . {get_piece_from_position(state, 3)} . {get_piece_from_position(state, 4)}{nl}\
     {get_piece_from_position(state, 5)} . {get_piece_from_position(state, 6)} . {get_piece_from_position(state, 7)} . {get_piece_from_position(state, 8)} .{nl}\
     . {get_piece_from_position(state, 10)} . {get_piece_from_position(state, 11)} . {get_piece_from_position(state, 12)} . {get_piece_from_position(state, 13)}{nl}\
    {get_piece_from_position(state, 14)} . {get_piece_from_position(state, 15)} . {get_piece_from_position(state, 16)} . {get_piece_from_position(state, 17)} .{nl}\
     . {get_piece_from_position(state, 19)} . {get_piece_from_position(state, 20)} . {get_piece_from_position(state, 21)} . {get_piece_from_position(state, 22)}{nl}\
    {get_piece_from_position(state, 23)} . {get_piece_from_position(state, 24)} . {get_piece_from_position(state, 25)} . {get_piece_from_position(state, 26)} .{nl}\
     . {get_piece_from_position(state, 28)} . {get_piece_from_position(state, 29)} . {get_piece_from_position(state, 30)} . {get_piece_from_position(state, 31)}{nl}\
    {get_piece_from_position(state, 32)} . {get_piece_from_position(state, 33)} . {get_piece_from_position(state, 34)} . {get_piece_from_position(state, 35)} .{nl}\
    ')



def update_board_submove(state, submove, piece):
    print('a')
    print(state)
    state[piece].remove(submove[0])
    state['-'].append(submove[0])
    state[piece].append(submove[1])
    state['-'].remove(submove[1])
    print('b')
    return state



# starting game
state = initial_game()
draw_board(board)
while not game_over(board):

    #play computer - ninitially computer will be x piece
    move = computer_play(board, 'x')
    if is_valid_move(board, move, 'x'):
        state = update_board(board, move, 'x')
    if game_over(board):
        break

    draw_board(board)
    #play player
    move = get_user_move()
    if is_valid_move(board, move, 'o'):
        state = update_board(board, move, 'o')


print(f'The winner is {winner(board)}')