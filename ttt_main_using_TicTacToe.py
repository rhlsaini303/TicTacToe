from TicTacToe import TTT_Board

gamemode="non-interactive"

while(gamemode=="interactive"):
	print("|X|X|X|\n|X|X|X|\n|X|X|X|")
	
	print("Do you wanna play tic-tac-toe (Answer Y/y/Yes/yes for yes):", end=" ")
	player_willingness=input()
	gameBoard=TTT_Board()

	while(player_willingness in ["Y","y","Yes","yes"]):
		result=gameBoard.play_game()
		print(result[1])

		print("Do you wanna play another game of tic-tac-toe (Answer Y/y/Yes/yes for yes):", end=" ")
		player_willingness=input()
	break #explicit termination of the loop

if(gamemode=="non-interactive"):
	gameBoard=TTT_Board()
	gameBoard.play_game(gamemode, "moves.txt")

print("Thanks for trying out Tic Tac Toe Console. HOPE YOU ENJOYED IT :)")
