import time

UI_wait = 0

choices = ('rock', 'paper', 'scissors')

#Read x : y as x beats y			
win_table_dict = {
			'rock' : 'scissors',
			'paper': 'rock',
			'scissors': 'paper'
			}		

def print_wait(to_print):
	print(to_print)
	time.sleep(UI_wait)