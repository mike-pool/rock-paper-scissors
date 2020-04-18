import random

from definitions import *

class player:
	def __init__(self):
		self.name = ''
		self._selection = ''
	
	@property
	def selection(self):
		return self._selection

	@selection.setter
	def selection(self, value):
		self._selection = choices[value]
		#!!handle string input
	
class human_player(player):
	def __init__(self):			
		super().__init__()
		self.name = 'Human'
	
class computer_player(player):
	def __init__(self):
		super().__init__()
		self.name = 'The computer'
	
	def make_selection(self):
		player.selection.fset(self, random.randint(0,2))
		#super().selection.fset(self, random.randint(0,2)) why isn't this the same as above?
		

if __name__ == '__main__':
	human = human_player()
	human.selection = 1
	print('HUMAN')
	print(human.selection)
	print()
	
	print('COMP')
	comp = computer_player()
	comp.make_selection()
	print(comp.selection) #why none?