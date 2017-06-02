# Created by alex 
# on 6/2/17

"""
Rock Paper Scissors with AI
"""
import random


def CPUPlay(choices, pastMoves):
	"""
	CPUPlay generates computer's move based on previous players moves.
	
	The CPU makes a choice based on how many times a player plays a choice, the CPU will play the weakness to the most
	played choice of the player. If the player has not made a choice or not enough data is had it will choose randomly
	using random.choice()
	
	Parameters
	==========
	:param choices: tuple
			Possible combinations of moves, ie rock, paper, scissors
	:param pastMoves: Dictionary
			Past moves of player, in format pastMoves = {'rock': #, 'paper': #, 'scissors': #}, where # is the recorde
			player moves number

	Returns
	=======
	:return weakness: String
			Returns the string the CPU will be playing based on what is weak to what and what choice the user makes most
	"""
	
	v = list(pastMoves.values())
	
	weakness = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
	
	if v.count(max(v)) > 1 or sum(v) < 3:
		return random.choice(choices)
	
	else:
		for key in pastMoves:
			if pastMoves[key] == max(v):
				return weakness[key]
	

def whoWon(player, cpu, scores):
	"""
	Function to decide who wins the game and updates score.
	
	Parameters
	==========
	:param player: String
			Players input
	:param cpu: String
			CPUs choice
	:param scores: Dictionary
			Dictionary holding scores of both player and CPU
	
	Returns
	=======
	:return: String
			Returns a string of whether it was a Tie, the player won, or the CPU won.
	"""
	
	strength = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
	
	if player == cpu:
		return "Tie."
	
	elif strength[player] == cpu:
		scores['player'] += 1
		return "You win!"
	
	else:
		scores['CPU'] += 1
		return "You lose."

def mainGame():
	"""
	
	Main game loop, type rock, paper, or scissors to play the CPU. Type quit to stop playing.
	
	"""
	
	playing = True
	
	scores = {'player': 0, 'CPU': 0}
	pastMoves = {'rock': 0, 'paper': 0, 'scissors': 0}
	choices = 'rock', 'paper', 'scissors'
	
	while playing:
		playerMove = ''
		
		while playerMove not in choices:
			playerMove = input('Rock, paper, scissors:\n').lower()
			
			if playerMove == 'quit' or playerMove == 'stop':
				playing = False
				break
		
		if playing:
			CPUMove = CPUPlay(choices, pastMoves)
			
			print("Computer chooses " + CPUMove + "!", whoWon(playerMove, CPUMove, scores), "CPU: " + str(scores['CPU'])
			      + " You: " + str(scores['player']), sep='\n', end='\n\n')
			
			pastMoves[playerMove] += 1
			
if __name__ == '__main__':
	mainGame()
