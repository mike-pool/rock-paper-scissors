import random

from definitions import *

class player:
	def set_selection(self, selection):
		self.selection = selection
		
	def get_selection(self):
		return self.selection
	
	def set_name(self, name):
		self.name = str(name)
	
	def get_name(self):
		return self.name	

class computer_player(player):
	def __init__(self):
		self.set_name('The computer')
	
	def make_selection(self):
		self.set_selection(make_selection_str(random.randint(0,2)))
		
class human_player(player):
	pass