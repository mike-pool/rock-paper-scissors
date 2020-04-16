ROCK = 0
PAPER = 1
SCISSORS = 2

choices_list = ['rock', 'paper', 'scissors']
choices = {choices_list[i] : i for i in range(len(choices))}

def make_selection_int(string_in):
	return choices(string_in)
	#!!Handle int input as well

def make_selection_str(int_in):
	for string, value in choices.items():
		if value == int_in:
			return string
			break
	return 'NA'
	#!!Handle str input as well