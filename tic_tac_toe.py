# BASIC VARIABLES
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
empty_squares = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winning_combs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
symbols = ['X', 'O']
# separators
sep1 = "============================================"
sep2 = "--------------------------------------------"

# INTRODUCTION - say hello, game rules
def print_intro():
	print(f'''				Tic Tac Toe
{sep1}
				GAME RULES:
Each player can place one stone per turn
on the 3x3 grid. The squares have numbers 
from 1 to 9. The WINNER is who succeeds in 
placing three of their stones in a:
* horizontal,
* vertical or
* diagonal row
{sep1}
			Let's start the game
{sep2}''')

# FORMATTED BOARD
def show_board():
	line_1 = '|{:^3}|{:^3}|{:^3}|'.format(board[0], board[1], board[2])
	line_2 = '|{:^3}|{:^3}|{:^3}|'.format(board[3], board[4], board[5])
	line_3 = '|{:^3}|{:^3}|{:^3}|'.format(board[6], board[7], board[8])
	edge = '+---+---+---+'
	print('{0:^44}'.format(edge),
		  '\n{0:^44}'.format(line_1),
		  '\n{0:^44}'.format(edge),
		  '\n{0:^44}'.format(line_2),
		  '\n{0:^44}'.format(edge),
		  '\n{0:^44}'.format(line_3),
		  '\n{0:^44}'.format(edge)
		  )
	print(sep1)

# PLAYER INPUT
def player_input(player):
	try:
		position = int(input(f'Player {symbols[player]} | Please enter your move number: ')) - 1
		if board[position] == 'X' or board[position] == 'O':
			print("This position is already taken!")
			player_input(player)
		else:
			empty_squares.remove(position)
			board[position] = symbols[player]
			print(sep1)
			return 1
	except ValueError:
		print("Invalid choice! You can type only numbers 1-9 ;)")
		player_input(player)
	except IndexError:
		print("Invalid choice! You can type only numbers 1-9 ;)")
		player_input(player)

# WHO WON? FUNCTION
def is_winner():
	for seq in winning_combs:
		square = board[seq[0]]
		if square != ' ':
			someone_won = True
			for char in seq:
				if board[char] != square:
					someone_won = False
					break
			if someone_won:
				if square == symbols[0]:
					print('{0:^44}'.format('Congratulations, the player X WON!'))
				else:
					print('{0:^44}'.format('Congratulations, the player O WON!'))
				break
		else:
			someone_won = False

	if not someone_won:
		return True
	else:
		return False

# PLAY FUNCTION
def main():
	print_intro()
	player = 0
	while empty_squares and is_winner():
		show_board()
		player_input(player)
		player = int(not player)
	if not empty_squares:
		print("DRAW!")


main()
