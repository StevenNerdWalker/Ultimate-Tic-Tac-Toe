# **GUIDE TO THE CODE**

## **Arguments**

The arguments/parameters most frequently used are:

### board

A tuple containing 3 lists representing the lines; each line containing 3 more lists representing the squares; each square containing 3 lists representing its lines, each containing 3 strings representing the state of each square ('X', 'O', or ' ')
([square, square, square], -> line 1
 [square, square, square], -> line 2
 [square, square, square]) -> line 3

### square

A list containing 3 lists representing its lines, each containing 3 strings representing the state of each square ('X', 'O', or ' ')
[[str, str, str],
 [str, str, str],
 [str, str, str]]

### square_to_play

A tuple representing a small board in the main board as a cartesian coordinate (x, y) beginning from the top left corner (0, 0) and going to (2, 2) on the bottom right corner. Values for x and y range from 0 to 2. It will be frequently used to determine the board in which a move will be played, such as board\[square_to_play\[1]][square_to_play\[0]]. Note that first we use the y value and then the x value as the index, because the board is organized by its lines, and then the squares in each line.

(0, 0) | (1, 0) | (2, 0)
\-----------------------
(0, 1) | (1, 1) | (2, 1)
\-----------------------
(0, 2) | (1, 2) | (2, 2)

### move

Works the same way as square_to_play, representing a coordinate (x, y), the only difference is it isn't the coordinate of a board, but of a square on the board the player will play.

### player

A string representing the current player/the player the function will operate for. It can be either 'X' or 'O'

'X' or 'O'

### turn

An integer representing the number of the turn in the game. Its modulo by 2 is used to determine wheter it is X's turn or O's turn to play

These arguments are used only in the minimax_score function

### depth, max_depth

Integers representing the current and the maximum depth of recursion, respectively

### maxing_player

Boolean (True or False) indicating wheter the algorythm should be trying to maximize or minimize the score

## **Functions**

### print_board(board, square_to_play, turn) -> None

Prints the current board on the terminal in text format

### get_square_winner(square) -> 'X'|'O'|'Draw'|None

Checks whether a square/board has been won or ended, and, if so, returns the winner; else, returns None

### get_board_winner(board) -> 'X'|'O'|'Draw'|None

Checks whether the board has been won or ended, and, if so, returns the winner; else, returns None

### make_move(board, square_to_play, move, player) -> board

Applies a move to a board and returns the new board, not altering the original one

### move_isValid(board, square_to_play, move) -> True|False

Check if a given move is valid on the board, returning a boolean value. Used mainly for dealing with human/user input

### find_valid_moves(board, square_to_play) -> \[tuple]

Returns a list with tuples contaning all of the valid moves on a given board. The tuples consist of (move, square_to_play). The second element of the tuple is there just in case the player was sent to an already won square and can play anywhere

### get_opponent(player) -> 'X'|'O'

Returns the opponent of the given player (X is O's opponent and vice-versa)

### minimax_score(board, square_to_play, player, depth, max_depth, maxing_player) -> int

Utilizes the minimax algorithm to assign a value to a certain board configuration given the player that will play in it. Can be used to find the optimal moves in a configuration. Better explained by [Sebastian Lague](https://www.youtube.com/watch?v=l-hh51ncgDI) and [Dan Shiffman](https://www.youtube.com/watch?v=trKjYdBASyQ). Code for this algorithm has been inspired from Robert Heaton's article on a [Tic-tac-toe AI](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-b/)

### human_ai(board, square_to_play, player=None) -> tuple(move, square_to_move)

Gets an input from the user for the move and, if necessary, the square to play the move in, and returns these in a tuple

### random_ai(board, square_to_play, player=None) -> tuple(move, square_to_move)

Returns a random move from all the valid moves in a given board. Has the argument player=None just to fit the interface for the artificial intelligences/functions that return a move

### minimax_ai(board, square_to_play, player) -> tuple(move, square_to_move)

Utilizes the minimax_score function to evaluate all the scores for each of the boards resulting from each possible move and returns the best scoring moves. If there are multiple moves with the best score, it randomly selects one of them as to not play the same game every time

### game() -> 'X'|'O'|'Draw'

Contains the main game loop, managing the turn logic and keeping track of the turn and square_to_play
