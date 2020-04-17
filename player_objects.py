import definitions

class player:
	def set_selection(selection):
		selection = selection
		
	def get_selection():
		return selection
	
	def set_name(self, name):
		name = str(name)
	
	def get_name():
		return name	

class computer_player(player):
	def __init__(self):
		self.set_name('The computer')
	
	def make_selection():
		set_selection(make_selection_str(random.randint(0,2)))
		
class human_player(player):
	pass