import random
import time
board = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def show_board(board):
	print(f'| {board[1]} | {board[2]} | {board[3]} |')
	print(f'| {board[4]} | {board[5]} | {board[6]} |')
	print(f'| {board[7]} | {board[8]} | {board[9]} |\n')
	


def players_turn(board):
	while True:
		try:
			number = int(input('Your turn: '))
			time.sleep(1)
		
			if board[number] == ' ':
				board[number] = 'X'
				print(f'\033[1;33mYou chose position {number}\033[0m')
				show_board(board)
				break
			
			else: 
				print('\033[1;31mPosition already occupied, try another!\033[0m')
				show_board(board)
				
		except (ValueError, KeyError):
			print('\033[1;31mOnly numbers between 1 and 9 are allowed.\033[0m')
			show_board(board)

			
									
def computers_turn(board):
	rand = random.randint(1, 9)
	while True:
		if board[rand] != ' ':
			rand = random.randint(1, 9)
		elif board[rand] == ' ':
			break
			
	print("Computer's turn: ")
	time.sleep(1)
	board[rand] = 'O'
	print(f'\033[1;33mComputer chose position {rand}\033[0m')
	show_board(board)
	


def win_condition(board, symbol):
	if board[1] == symbol and board[2] == symbol and board[3] == symbol:
		return True

	elif board[4] == symbol and board[5] == symbol and board[6] == symbol:
	    return True
	
	elif board[7] == symbol and board[8] == symbol and board[9] == symbol:
	    return True
	
	elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
	    return True
	
	elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
	    return True
	
	elif board[3] == symbol and board[6] == symbol and board[9] == symbol:
	    return True
	
	elif board[1] == symbol and board[5] == symbol and board[9] == symbol:
	    return True
	
	elif board[3] == symbol and board[5] == symbol and board[7] == symbol:
	    return True
	
	return False
		


def main():
	print('\033[1;29mChoose one of the numbers to make a move.\033[0m')
	print(f'| {1} | {2} | {3} |')
	print(f'| {4} | {5} | {6} |')
	print(f'| {7} | {8} | {9} |')
	while True:
		
		players_turn(board)
		
		if win_condition(board, 'X'):
			print('\033[1;32mCongratulations, you won!\n(the computer is dumb!)\033[0m')
			print('')
			break
		
		if ' ' not in board.values():
			print('\033[1;244mDraw\033[0m')
			break
		
		computers_turn(board)
			
		if win_condition(board, 'O'):
			print('\033[1;31mComputer won!\033[0m')
			break
			


if __name__ == '__main__':
	main()