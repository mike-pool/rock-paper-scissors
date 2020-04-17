from definitions import *
from player_objects import *
		
class rock_paper_scissors_games:

	def __init__(self):
		self.initialize_game()
		
	def initialize_game(self):
		self.human = human_player()
		self.computer = computer_player()
		print('')
		print_wait('Welcome to Rock, Paper, Scissors!\n')
		self.human.name = input('Please enter a player name: ')
		time.sleep(UI_wait)
	
	def conduct_round(self):
		self.computer.make_selection()
		self.human.selection = input('Choose rock, paper, or scissors: ')
		#!!Handle integer and erroneous inputs
		time.sleep(UI_wait)
		print('')
		winner = self.resolve_shoot(self.human, self.computer)
		print_wait('You chose {}.'.format(self.human.selection))
		print_wait('The computer chose {}.\n'.format(self.computer.selection))
		if winner != 'tie':
			print_wait(f'{winner} won!\n')
		else:
			print_wait('Tie!\n')
		
	def resolve_shoot(self, player0, player1):
		p0 = player0.selection
		p1 = player1.selection
		
		if p0 == p1:
		#Same selection is tie
			return 'tie'
		else:
			if win_table_dict[p0] == p1:
			#Player 0 selection is winner and player 1 selection is loser
				return player0.name
			else:
			#Only other possibility aside from a tie is a loss for player 0
				return player1.name
		
	def end_game(self):
		name = self.human.name
		print_wait(f'Thanks for playing, {name}!')