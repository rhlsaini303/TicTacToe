class TTT_Board:
	__three_crosses=['X','X','X']
	__three_zeroes=['0','0','0']

	def __init__(self):
		self.board=Board=['|',' ','|',' ','|',' ','|','\n',
							'|',' ','|',' ','|',' ','|','\n',
							'|',' ','|',' ','|',' ','|','\n']

		self.pos_to_idx={'1':1, '2':3, '3':5, '4':9, '5':11, '6':13, '7':17, '8':19, '9':21}
		self.pos_available=['1','2','3','4','5','6','7','8','9']
		self.turn_number=0

		self.board_state=("Empty Board", "No ongoing game")

	def __initialise_board(self):
		for i in self.pos_to_idx.values():
			self.board[i]=" "

		self.pos_available=['1','2','3','4','5','6','7','8','9']
		self.turn_number=0
		self.board_state=("Empty Board", "No ongoing game")

	def __print_board(self):
		for i in self.board:
			print(i, end="")

	def __diagonal_match(self):
		principal_diagonal=[self.board[self.pos_to_idx['1']], self.board[self.pos_to_idx['5']], self.board[self.pos_to_idx['9']]]
		if(principal_diagonal==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(principal_diagonal==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		second_diagonal=[self.board[self.pos_to_idx['7']], self.board[self.pos_to_idx['5']], self.board[self.pos_to_idx['3']]]
		if(second_diagonal==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(second_diagonal==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		return ("Match Not Found", "Continue")

	def __horizontal_match(self):
		first_row=[self.board[self.pos_to_idx['1']], self.board[self.pos_to_idx['2']], self.board[self.pos_to_idx['3']]]
		if(first_row==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(first_row==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		second_row=[self.board[self.pos_to_idx['4']], self.board[self.pos_to_idx['5']], self.board[self.pos_to_idx['6']]]
		if(second_row==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(second_row==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		third_row=[self.board[self.pos_to_idx['7']], self.board[self.pos_to_idx['8']], self.board[self.pos_to_idx['9']]]
		if(third_row==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(third_row==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		return ("Match Not Found", "Continue")


	def __vertical_match(self):
		first_col=[self.board[self.pos_to_idx['1']], self.board[self.pos_to_idx['4']], self.board[self.pos_to_idx['7']]]
		if(first_col==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(first_col==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		second_col=[self.board[self.pos_to_idx['2']], self.board[self.pos_to_idx['5']], self.board[self.pos_to_idx['8']]]
		if(second_col==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(second_col==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		third_col=[self.board[self.pos_to_idx['3']], self.board[self.pos_to_idx['6']], self.board[self.pos_to_idx['9']]]
		if(third_col==self.__three_crosses):
			return ("Match Found", "Player 2 won the Match")
		elif(third_col==self.__three_zeroes):
			return ("Match Found", "Player 1 won the Match")

		return ("Match Not Found", "Continue")

	def __check_for_result(self):
		diagonal_result=self.__diagonal_match()
		if(diagonal_result[0]=="Match Found"):
			return ("Game Decided", diagonal_result[1])

		horizontal_result=self.__horizontal_match()
		if(horizontal_result[0]=="Match Found"):
			return ("Game Decided", horizontal_result[1])

		vertical_result=self.__vertical_match()
		if(vertical_result[0]=="Match Found"):
			return ("Game Decided", vertical_result[1])

		return ("Game Undecided", "Continue to next step")

	def __execute_turn(self, gamemode="interactive", move=None):
		if(gamemode=="interactive"):
			if(self.turn_number%2==1): #First player's turn
				print("Player 1 enter your choice of position to place a 0:", end=" ")
				zero_pos = input()
				
				if(zero_pos in self.pos_available):
					self.board[self.pos_to_idx[zero_pos]]="0"
					self.pos_available.remove(zero_pos)
				else:
					print('''You entered an invalid position.\n 
						If you wan't to continue, enter a valid position otherwise press any other key to abort:''', end=" ")
					zero_pos = input()
					
					if(zero_pos in self.pos_available):
						self.board[self.pos_to_idx[zero_pos]]="0"
						self.pos_available.remove(zero_pos)
					else:
						return ("Game Aborted","Game Aborted Midway by Player 1")
			else: #Second Player's turn
				print("Player 2 enter your choice of position to place an X:", end=" ")
				cross_pos = input()
				
				if(cross_pos in self.pos_available):
					self.board[self.pos_to_idx[cross_pos]]="X"
					self.pos_available.remove(cross_pos)
				else:
					print('''You entered an invalid position.\n 
						If you wan't to continue, enter a valid position otherwise press any other key to abort:''', end=" ")
					cross_pos = input()
					
					if(cross_pos in self.pos_available):
						self.board[self.pos_to_idx[cross_pos]]="X"
						self.pos_available.remove(cross_pos)
					else:
						return ("Game Aborted","Game Aborted Midway by Player 2")

			return ("Game Undecided", "Moving onto next turn.")
		elif(gamemode=="non-interactive"):
			if(self.turn_number%2==1): #First player's turn				
				self.board[self.pos_to_idx[move]]="0"
				self.pos_available.remove(move)
				
			else: #Second Player's turn
				self.board[self.pos_to_idx[move]]="X"
				self.pos_available.remove(move)

			return ("Turn executed sucessfully", "Nothing to Say")

	def play_game(self, gamemode="interactive", gamefile=None):
		if(gamemode=="interactive"):
			print("Note the positional values on the grids where you place your zeroes and crosses.")
			print("|1|2|3|\n|4|5|6|\n|7|8|9|\n")
			
			self.__initialise_board()
			self.board_state=("Game Undecided", "Ongoing Game")
			
			for self.turn_number in range(1,10,1):
				self.board_state=self.__execute_turn(gamemode)
				if(self.board_state[0]=="Game Aborted"):
					return self.board_state

				self.__print_board()

				if(self.turn_number > 4):
					self.board_state= self.__check_for_result()
					if(self.board_state[0]=="Game Decided"):
						return self.board_state

			self.board_state=("Game Decided","Game Ended in a DRAW")
			return self.board_state
		elif(gamemode=="non-interactive"):
			'''
			In non-interactive mode we also take a file as input.
			Each row of the input file must contain 9 values from 1 to 9, each 
			separated by a comma and the last one followed by an endline. In any 
			row, any integer value should appear only once. 
			'''

			try:
				moves_file=open(gamefile, mode="r", encoding="utf-8")
				result_file=open("results.txt", mode="w", encoding="utf-8")
			except BaseException as exp:
				print("Exception occurred while opening the file")
				raise exp
			else:
				'''
				Here we will read the file and store all the game choices and validate
				them before proceeding with them.
				'''

				for line in moves_file.readlines():
					turns=(line.rstrip("\n")).split(sep=",")

					#Now we validate the input
					if(sorted(turns)==['1','2','3','4','5','6','7','8','9']):
						#Now we can execute turns
						self.__initialise_board()
						self.board_state=("Game Undecided", "Ongoing Game")

						for self.turn_number in range(1,10,1):
							self.__execute_turn(gamemode, turns[self.turn_number-1])
							
							if(self.turn_number > 4):
								self.board_state= self.__check_for_result()
								if(self.board_state[0]=="Game Decided"):
									result_file.write(str(turns)+"-->"+str(self.board_state)+"\n")
									break
								elif(self.turn_number==9):
									self.board_state=("Game Decided","Game Ended in a DRAW")
									result_file.write(str(turns)+"-->"+str(self.board_state)+"\n")
								else:
									continue
					else:
						#The file has invalid content
						self.__initialise_board()
						result_file.write(str(turns)+"-->"+"(GAME ABORTED: The corresponding line in moves.txt file has invalid content.)\n")
						return ("Error Occurred", "GAMES ABORTED: The moves.txt file has invalid content.")

				return("Games Finished", "All the games have been played and the results have been written in results.txt file.")
					
