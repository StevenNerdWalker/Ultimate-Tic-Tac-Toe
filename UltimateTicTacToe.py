import random

#**********Basic Functions**********#


def print_board(board, square_to_play, turn):
    
    # Print the board
    l0, l1, l2 = board
    sq1, sq2, sq3 = l0
    sq4, sq5, sq6 = l1
    sq7, sq8, sq9 = l2

    print('\n'*2)
    for k in range(0, 3):
        for i in range(0, 3):
            for j in range(0, 3):
                if j < 2:   
                    print(' '.join(board[k][j][i]), end=' | ')
                else:
                    print(' '.join(board[k][j][i]), end='')
            print('\n', end='')
        if k < 2:
            print('=' * 21)
        else:
            print('\n')

    # Print the square to play in
    if square_to_play is None:
        print('Square to play: Any')

    else:
        x, y = square_to_play
        if x == 0:
            h = 'left'
        elif x == 1:
            h = 'middle'
        else:
            h = 'right'
        if y == 0:
            v = 'Top'
        elif y == 1:
            v = 'Middle'
        else:
            v = 'Bottom'

        if x == 1 and y == 1:
            print(f'Square to play: Middle')
        else:
            print(f'Square to play: {v} {h}')

    # Print the player
    if turn % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    print(f'Player: {player}')


def get_square_winner(square):
    l0, l1, l2 = square
    
    # Lines
    for line in square:
        if len(set(line)) == 1 and ' '  != line[0] :
            return line[0]

    # Columns
    for i in range(3):
        if ' ' != l0[i] == l1[i] == l2[i]:
            return l0[i]
    
    # Diagonals
    if ' ' != l0[0] == l1[1] == l2[2]:
        return l0[0]
    elif ' ' != l0[2] == l1[1] == l2[0]:
        return l0[2]

    # Draw
    for line in square:
        if ' ' in line:
            return None
    return 'Draw'


def get_board_winner(board):
    sq1 = get_square_winner(board[0][0])
    sq2 = get_square_winner(board[0][1])
    sq3 = get_square_winner(board[0][2])
    sq4 = get_square_winner(board[1][0])
    sq5 = get_square_winner(board[1][1])
    sq6 = get_square_winner(board[1][2])
    sq7 = get_square_winner(board[2][0])
    sq8 = get_square_winner(board[2][1])
    sq9 = get_square_winner(board[2][2])

    temp_board = ([sq1, sq2, sq3], [sq4, sq5, sq6], [sq7, sq8, sq9])
    for y in range(3):
        for x in range(3):
            if temp_board[y][x] is None:
                temp_board[y][x] = ' ' # sets the squares that havent been won as ' ' to not mess up the get_square_winner function

    return get_square_winner(temp_board)


def make_move(board, square_to_play, move, player):
    new_board = list(board)
    line, square = square_to_play

    # makes a copy of the square line
    new_sqline = board[line][square][move[1]].copy()

    # makes a copy of the square, and substitutes the original square line for the copy
    new_sq = board[line][square].copy()
    new_sq[move[1]] = new_sqline

    # makes a copy of the line, and substitutes the original square for the copy
    new_line = board[line].copy()
    new_line[square] = new_sq

    # substitutes the original line for the copy
    new_board[line] = new_line

    new_board[line][square][move[1]][move[0]] = player

    return tuple(new_board)


def make_move2(board, square_to_play, move, player):
    # iterates through the board and checks if it's at the list which will be altered, and then goes deeper into it to make a copy

    new_board = []
    for line in range(len(board)):
        temp_line = []
        if line != square_to_play[1]:
            temp_line.extend(board[line])
        else:

            for square in range(len(board[line])):
                temp_square = []
                if square != square_to_play[0]:
                    temp_square.extend(board[line][square])
                else:

                    for sq_line in range(len(board[line][square])):
                        temp_sqline = []
                        if sq_line != move[1]:
                            temp_sqline.extend(board[line][square][sq_line])
                        else:
                            temp_sqline = [x for x in board[line][square][sq_line]]
                            temp_sqline[move[0]] = player

                        temp_square.append(temp_sqline)
                
                temp_line.append(temp_square)
        
        new_board.append(temp_line)

    return new_board


def move_isValid(board, square_to_play, move):
    square = board[square_to_play[1]][square_to_play[0]]
    if get_square_winner(square) is None:
        if square[move[1]][move[0]] == ' ':
            return True
    return False


def find_valid_moves(board, square_to_play):

    # Selects every valid move on the whole board
    if square_to_play is None or get_square_winner(board[square_to_play[1]][square_to_play[0]]) is not None:
        valid_moves = []
        for sqy in range(3):
            for sqx in range(3):
                sq = board[sqy][sqx]
                if get_square_winner(sq) is None:
                    for y in range(3):
                        for x in range(3):
                            if sq[y][x] == ' ':
                                valid_moves.append(((x, y), (sqx, sqy)))

    # Selects every valid move on the square to be played
    else:
        valid_moves = []
        square = board[square_to_play[1]][square_to_play[0]]
        for y in range(3):
            for x in range(3):
                if square[y][x] == ' ':
                    valid_moves.append(((x, y), square_to_play))

    return valid_moves


def get_opponent(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def minimax_score(board, square_to_play, player, depth, max_depth, maxing_player):

    # If it's the maximizing player, adds 100 for every square it has won and reduces 100 points for every square the opponent has won
    # If it's the minimizing player, reduces 100 for every square it has won and adds 100 points for every square the opponent has won
    if depth == max_depth:
        
        winners = []
        for line in board:
            for sq in line:
                winner = get_square_winner(sq)
                if winner is not None and winner != 'Draw':
                    winners.append(winner)
        score = 0
        if maxing_player == True:
            for winner in winners:
                if winner == player:
                    score += 10
                else:
                    score -=10
        else:
            for winner in winners:
                if winner == player:
                    score -= 10
                else:
                    score += 10
        return score

    valid_moves = find_valid_moves(board, square_to_play)
    opponent = get_opponent(player)
    scores = []

    # Goes through every valid move, recusively calling itself until it reaches the maximum depth
    for move, sq_2_play in valid_moves:
        new_board = make_move(board, sq_2_play, move, player)
        score = minimax_score(board=new_board, square_to_play=move, player=opponent, depth=depth + 1, max_depth=max_depth, maxing_player=not maxing_player)
       
        scores.append(score)

    if maxing_player == True:
        return max(scores)
    else:
        return min(scores)


#**********Artificial Inteligences**********#

def human_ai(board, square_to_play, player=None):
    while True:

        # Get the square on the main board
        if square_to_play is None:
            # Get the square
            try:
                squareX = int(input("Big square to make your move's x coordinate:"))
                if not 0 <= squareX <= 2:
                    raise Exception
                squareY = int(input("Big square to make your move's y coordinate:"))
                if not 0 <= squareY <= 2:
                    raise Exception
            except:
                print('Invalid coordinate')
                continue
            # Check if it's valid
            try:
                if get_square_winner(board[squareY][squareX]) is not None:
                    raise Exception
            except:
                print("Big square can't be played on")
                continue
        else:
            squareX, squareY = square_to_play


        # Get move to be played in the square
        try:
            moveX = int(input("Square to make your move's x coordinate:"))
            if not 0 <= moveX <= 2:
                raise Exception
            moveY = int(input("Square to make your move's y coordinate:"))
            if not 0 <= moveY <= 2:
                raise Exception 
        except:
            print('Invalid coordinate')
            continue

        return ((moveX, moveY), (squareX, squareY))


def random_ai(board, square_to_play, player=None):
    valid_moves = find_valid_moves(board, square_to_play)

    index = random.randint(0, len(valid_moves)-1)
    return valid_moves[index]


def minimax_ai(board, square_to_play, player):
    valid_moves = find_valid_moves(board, square_to_play)

    if player == 'X':
        maxing = True
    else:
        maxing = False

    best_moves = []
    best_score = 0

    for move, square in valid_moves:
        new_board = make_move(board, square, move, player)
        score = minimax_score(new_board, move, get_opponent(player), 0, 5, not maxing)

        if score == best_score:
            best_moves.append((move, square))
        elif score > best_score:
            if maxing:
                best_moves = [(move, square)]
                best_score = score
        else:
            if not maxing:
                best_moves = [(move, square)]
                best_score = score

    if len(best_moves) == 0:
        return valid_moves[0]
    else:
        index = random.randint(0, len(best_moves)-1)
        return best_moves[index]


#**********The game**********#


def game():
    main_board = ([[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]], 
                [[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]], 
                [[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]])
    square_to_play = None

    turn = 0

    while True:
        print_board(main_board, square_to_play, turn)
        winner = get_board_winner(main_board)
        if winner is not None:
            return winner

        if turn % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        
        move, square_to_play = minimax_ai(board=main_board, square_to_play=square_to_play, player=player)

        main_board = make_move2(main_board, square_to_play, move, player)
        turn += 1
        square_to_play = move

        if get_square_winner(main_board[square_to_play[1]][square_to_play[0]]) is not None:
            square_to_play = None

print(f'\nWinner: {game()}')
#print_board(board=([[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]], 
 #               [[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]], 
  #              [[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]]), square_to_play=None, turn=0)
