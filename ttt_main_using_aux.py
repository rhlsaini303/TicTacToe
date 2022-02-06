from ttt_aux import *

while(True):
	print("|X|X|X|\n|X|X|X|\n|X|X|X|")
	
	print("Do you wanna play tic-tac-toe (Answer Y/y/Yes/yes for yes):", end=" ")
	player_willingness=input()
	
	while(player_willingness in ["Y","y","Yes","yes"]):
		game=play_a_ttt_game()
		print(game[1])

		print("Do you wanna play another game of tic-tac-toe (Answer Y/y/Yes/yes for yes):", end=" ")
		player_willingness=input()

	break

print("Thanks for trying out Tic Tac Toe Console. HOPE YOU ENJOYED IT :)")
