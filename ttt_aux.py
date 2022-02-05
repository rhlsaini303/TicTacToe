Board=['|','X','|','X','|','X','|','\n',
	'|','X','|','X','|','X','|','\n',
	'|','X','|','X','|','X','|','\n']
	
'''
	Indices of empty vars are: 
	|01|03|05|
	|09|11|13|
	|17|19|21|
'''
pos_to_idx = {'1':1, '2':3, '3':5, '4':9, '5':11, '6':13, '7':17, '8':19, '9':21}

def initialize_board():
	for i in pos_to_idx.values():
		Board[i]=" "

def print_board():
	for i in Board:
		print(i, end="")

def execute_turn(turn, pos_available):
	if(turn%2==1): #First player's turn
		print("Player 1 enter your choice of position to place a 0:", end=" ")
		zero_pos = input()
		
		if(zero_pos in pos_available):
			Board[pos_to_idx[zero_pos]]="0"
			pos_available.remove(zero_pos)
		else:
			print('''You entered an invalid position.\n 
				If you wan't to continue, enter a valid position otherwise press any other key to abort:''', end=" ")
			zero_pos = input()
			
			if(zero_pos in pos_available):
				Board[pos_to_idx[zero_pos]]="0"
				pos_available.remove(zero_pos)
			else:
				return ("Game Aborted","Game Aborted Midway by Player 1")
	else: #Second Player's turn
		print("Player 2 enter your choice of position to place an X:", end=" ")
		cross_pos = input()
		
		if(cross_pos in pos_available):
			Board[pos_to_idx[cross_pos]]="X"
			pos_available.remove(cross_pos)
		else:
			print('''You entered an invalid position.\n 
				If you wan't to continue, enter a valid position otherwise press any other key to abort:''', end=" ")
			cross_pos = input()
			
			if(cross_pos in pos_available):
				Board[pos_to_idx[cross_pos]]="X"
				pos_available.remove(cross_pos)
			else:
				return ("Game Aborted","Game Aborted Midway by Player 2")

	return ("Turn executed successfully", "Move onto next thing.")


three_crosses=['X','X','X']
three_zeroes=['0','0','0']


def diagnol_match():
	principal_diagonal=[Board[pos_to_idx['1']], Board[pos_to_idx['5']], Board[pos_to_idx['9']]]
	if(principal_diagonal==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(principal_diagonal==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	second_diagonal=[Board[pos_to_idx['7']], Board[pos_to_idx['5']], Board[pos_to_idx['3']]]
	if(second_diagonal==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(second_diagonal==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	return ("Match Not Found", "Continue")

def horizontal_match():
	first_row=[Board[pos_to_idx['1']], Board[pos_to_idx['2']], Board[pos_to_idx['3']]]
	if(first_row==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(first_row==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	second_row=[Board[pos_to_idx['4']], Board[pos_to_idx['5']], Board[pos_to_idx['6']]]
	if(second_row==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(second_row==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	third_row=[Board[pos_to_idx['7']], Board[pos_to_idx['8']], Board[pos_to_idx['9']]]
	if(third_row==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(third_row==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	return ("Match Not Found", "Continue")


def vertical_match():
	first_col=[Board[pos_to_idx['1']], Board[pos_to_idx['4']], Board[pos_to_idx['7']]]
	if(first_col==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(first_col==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	second_col=[Board[pos_to_idx['2']], Board[pos_to_idx['5']], Board[pos_to_idx['8']]]
	if(second_col==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(second_col==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	third_col=[Board[pos_to_idx['3']], Board[pos_to_idx['6']], Board[pos_to_idx['9']]]
	if(third_col==three_crosses):
		return ("Match Found", "Player 2 won the Match")
	elif(third_col==three_zeroes):
		return ("Match Found", "Player 1 won the Match")

	return ("Match Not Found", "Continue")

def check_board_for_result():
	diagonal_result=diagnol_match()
	if(diagonal_result[0]=="Match Found"):
		return ("Game Decided", diagonal_result[1])

	horizontal_result=horizontal_match()
	if(horizontal_result[0]=="Match Found"):
		return ("Game Decided", horizontal_result[1])

	vertical_result=vertical_match()
	if(vertical_result[0]=="Match Found"):
		return ("Game Decided", vertical_result[1])

	return ("Game Undecided", "Continue")

	
def play_a_ttt_game():
	print("Note the positional values on the grids where you place your zeroes and crosses.")
	print("|1|2|3|\n|4|5|6|\n|7|8|9|")
	
	initialize_board()
	pos_available=['1','2','3','4','5','6','7','8','9']
	
	for turn in range(1,10,1):
		turn_result=execute_turn(turn, pos_available)
		if(turn_result[0]=="Game Aborted"):
			return turn_result

		print_board()

		if(turn > 4):
			game_result=check_board_for_result()
			if(game_result[0]=="Game Decided"):
				return game_result

	return ("No Winner", "Game Ended in a DRAW")



