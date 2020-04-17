import random

from definitions import *

class player:
	def __init__(self):
		self.set_name = ''
		self.selection = ''

class computer_player(player):
	def __init__(self):
		super().__init__()
		self.name = 'The computer'
	
	def make_selection(self):
		self.selection = make_selection_str(random.randint(0,2))
		#!!Function converting int to string should be contained in class - parent class as it's valid for all player types
		
class human_player(player):
	def __init__(self):
		super().__init__()
		self.set_name = 'Human'