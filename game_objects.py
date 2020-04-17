import time

from definitions import *
from player_objects import *
		
class game:

	def __init__(self):
		self.initialize_game()
		
	def initialize_game(self):
		self.human = human_player()
		self.computer = computer_player()
		print('Welcome to Rock, Paper, Scissors!\n')
		#time.sleep(2)
		self.human.set_name(input('Please enter a player name: '))
		#time.sleep(2)
	
	def conduct_round(self):
		self.computer.make_selection()
		self.human.set_selection(input('Choose rock, paper, or scissors: '))
		#!!Handle erroneous inputs
		winner = self.resolve_shoot(self.human, self.computer)
		print('You chose {}.\n'.format(self.human.get_selection()))
		#time.sleep(2)
		print('The computer chose {}.\n'.format(self.computer.get_selection()))
		#time.sleep(2)
		if winner != 'NA':
			print(f'{winner} won!\n')
		else:
			print('Tie!\n')
		#time.sleep(2)
		
	def resolve_shoot(self, player0, player1):
		p0 = player0.get_selection()
		p1 = player1.get_selection()
		
		print(f'P0: {p0}\n')
		print(f'P1: {p1}\n')
		
		if p0 == p1:
			return 'NA'
		else:
			for i in win_table:
				print(f'{i} 0: {i[0]}\n')
				print(f'{i} 1: {i[1]}\n')
				if p0 == i[0] and p1 == i[1]:
				#Player 0 selection is winner and player 1 selection is loser
					return player0.get_name()
			#Only other possibility aside from a tie is a loss for player 0
			return player1.get_name()
		
	def end_game(self):
		name = self.human.get_name()
		print(f'Thanks for playing, {name}!')