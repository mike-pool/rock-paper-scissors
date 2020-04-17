import time

UI_wait = 1

chioces_list = ['rock', 'paper', 'scissors']
chioces = {chioces_list[i] : i for i in range(len(chioces_list))}

#Read x : y as x beats y			
win_table_dict = {
			'rock' : 'scissors',
			'paper': 'rock',
			'scissors': 'paper'
			}		
			
def make_selection_int(string_in):
	return chioces(string_in)
	#!!Handle int input as well

def make_selection_str(int_in):
	for string, value in chioces.items():
		if value == int_in:
			return string
			break
	return 'NA'
	#!!Handle str input as well

def print_wait(to_print):
	print(to_print)
	time.sleep(UI_wait)