import time

from game_objects import game
from definitions import UI_wait

play = 'yes'
mygame = game()

play = input('Hi {}! Would you like to play a round? (Yes/ No): '.format(mygame.human.get_name()))
time.sleep(UI_wait)

while play == 'yes':
	mygame.conduct_round()
	play = input('Would you like to play again? (Yes/ No): ').lower()
	time.sleep(UI_wait)

mygame.end_game()