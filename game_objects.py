import time
import random

from definitions import *
from player_objects import *
		
class game:
	test = 1
	
	def __init__(self):
		self.initialize_game()
		
	def initialize_game(self):
		self.test_init = game.test + 2
		self.human = human_player()
		self.computer = computer_player()
		print('Welcome to Rock, Paper, Scissors!\n')
		time.sleep(2)
		human.set_name(input('Please enter a player name: '))
		time.sleep(2)
	
	def conduct_round():
		computer.make_selection()
		human.set_selection(input('Choose Rock, Paper, or Scissors.\n'))
		#!!Handle erroneous inputs
		winner = resolve_shoot(human, computer)
		print('You chose {f}.\n'.human.get_selection())
		time.sleep(2)
		print('The computer chose {f}.\n'.computer.get_selection())
		time.sleep(2)
		if winner != 'NA':
			print(f'{winner} won!\n')
		else:
			print('Tie!\n')
		time.sleep(2)
		
	def resolve_shoot(player0, player1):
		p0 = player0.get_selection()
		p1 = player1.get_selection()
		
		if p0 == p1:
			return 'NA'
		else:
			for i in win_table:
				if p0 == i[0] and p1 == i[1]:
				#Player 0 selection is winner and player 1 selection is loser
					return player0.get_name()
				else:
				#Only other possibility aside from a tie is a loss for player 0
					return player1.get_name()
		
	def end_game():
		name = human.get_name()
		print(f'Thanks for playing, {name}!')