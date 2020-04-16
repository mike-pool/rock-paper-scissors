import time
import definitions
import random


		
class game:
	def __init__():
		initialize_game()
		
	def initialize_game():
		print('Welcome to Rock, Paper, Scissors!\n')
		human = human_player()
		computer = computer_player()
		time.sleep(2)
		human.set_name(input('Please enter a player name.\n'))
	
	def conduct_round():
		computer.make_selection()
		human.set_selection(make_selection_int(input('Choose Rock, Paper, or Scissors.\n'')))
		#!!Handle erroneous inputs
		winner = resolve_shoot(human, computer):
		print('You chose {f}.\n'.make_selection_str(player0.get_selection()))
		time.sleep(2)
		print('The computer chose {f}.\n'.make_selection_str(player1.get_selection()))
		time.sleep(2)
		if winner != 'NA':
			print(f'{winner} won!\n')
		else
			print('Tie!\n')
		time.sleep(2)
		
	def resolve_shoot(player0, player1):
		sel0 = player0.get_selection_int()
		sel1 = player1.get_selection_int()
		
		if sel0 == ROCK:
			if sel1 == ROCK:
				winner = string
			
		
		return winner
		
	def end_game():
		name = human.get_name()
		print(f'Thanks for playing {name}!')
		
	
class player:
	def set_selection(selection):
		selection = selection
		
	def get_selection():
		return selection
	
	def set_name(name):
		name = str(name)
	
	def get_name
		return name	

class (player)computer_player:
	def __init__():
		set_name('The computer')
	
	def make_selection():
		set_selection(random.randint(0,2))
		
class (player)human_player:
	
