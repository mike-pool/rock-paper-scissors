import random

from definitions import *

class player:
	def __init__(self):
		self.name = ''
		self._selection = ''
	
	@property
	def selection(self):
		return self._selection
		print('getting')

	@selection.setter
	def selection(self, value):
		self._selection = choices[0]
		print('setting ' + choices[0])
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
		self._selection = player.selection.fset(self, random.randint(0,2))
		print(self.selection)
		

if __name__ == '__main__':
	human = human_player()
	human.selection = 1
	print(human.selection) #why no 'getting' printed?

	comp = computer_player()
	comp.make_selection()
	print(comp.selection) #why none?