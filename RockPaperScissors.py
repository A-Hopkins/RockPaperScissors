# Created by alex 
# on 6/2/17

"""
Rock Paper Scissors with AI
"""


def CPUPlay(choices, pastMoves):
	pass


def whoWon(playerMove, CPUMove, scores):
	pass


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
			
			if playerMove == 'quit':
				playing = False
				break
		
		if playing:
			CPUMove = CPUPlay(choices, pastMoves)
			
			print("Computer chooses " + CPUMove + "!", whoWon(playerMove, CPUMove, scores), "CPU: " + str(scores['CPU'])
			      + " You: " + str(scores['player']), sep='\n', end='\n\n')
			
			pastMoves[playerMove] += 1
			
if __name__ == '__main__':
	mainGame()
