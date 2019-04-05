#!/bin/bash/env python

"""
	Popular game for toddlers, Tic Tac Toe
	The player who succeeds in placing three of their marks in a horizontal,
	vertical, or diagonal row wins the game. 
"""

# import numpy library for matrix operations

import numpy as np

def start():
	
	print('Welcome to the Tic Tac Toe Game!')

	player1 = ''
	player2 = ''

	# board is represented as matrix 3x3

	board = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])

	# positions translated into matrix positions via tuples of indexes
	
	pos = {
			1: (2,0),
			2: (2,1),
			3: (2,2),
			4: (1,0),
			5: (1,1),
			6: (1,2),
			7: (0,0),
			8: (0,1),
			9: (0,2)

	}
	

	
	# ask first player for marker ('X' or 'O')

	while (player1!='X') and (player1!='O'):
		player1 = str(input("Choose between X and O: ")).upper()

	if player1 == 'X':
		player2 = 'O'
	else:
		player2= 'X'

	numbers = [1,2,3,4,5,6,7,8,9] # available positions update

	# Player 1 plays and then player 2

	while True:

		try:
			position = 0

			# Player 1

			print('\nPlayer 1\n')
			while position<1 or position>9:
				position = int(input("Choose position (1-9): "))
				if position in numbers:	#check if position already taken
					board[pos[position]] = player1
					numbers.remove(position) # update numbers
					break
				continue
			
			board_display(board) # display board
			
			if win_check(board,player1): # check if there's a winning combination
				print('Congradulations player 1 wins!')
				break
			elif numbers==[]:	# check if every position is taken
				print("It's a tie!\n")
				break	 
			position = 0 
			

			# Player 2 same as player 1

			print('\nPlayer 2\n')
			while position<1 or position>9:
				position = int(input("Choose position (1-9): "))
				if position in numbers:
					board[pos[position]] = player2
					numbers.remove(position)
					break
				continue
		
			board_display(board)
			
			if win_check(board,player2):
				print('Congradulations player 2 wins!')
				break 
			elif numbers==[]:
				print("It's a tie!\n")
				break
			
		except:
			pass

	# Ask for replay
	replay()

# Displaying the board as it is

def board_display(board):
	print('{}|{}|{}'.format(board[0][0],board[0][1],board[0][2]))
	print('------')
	print('{}|{}|{}'.format(board[1][0],board[1][1],board[1][2]))
	print('------')
	print('{}|{}|{}'.format(board[2][0],board[2][1],board[2][2]))


# Checking for the winner after every play

def win_check(board,marker):
	
	# Checking all the cases if player won
	if(all(board[0]==marker) 
		or all(board[1]==marker) 
		or all(board[2]==marker) 
		or all(board[:,0]==marker)
		or all(board[:,1]==marker)
		or all(board[:,2]==marker)
		or (board[0][0]==marker and board[1][1]==marker and board[2][2]==marker) 
		or (board[0][2]==marker and board[1][1]==marker and board[2][0]==marker)):
		return True
	else:
		return False

# Replay function that starts game again if players want to play again

def replay():
	ans = input('Do you want to play it again? Y/N').lower()
	if(ans=='y'):
		start()
	print('Thanks for playing!')

# Start game
start()

