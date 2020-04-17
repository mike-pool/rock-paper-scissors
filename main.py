from game_objects import game
import time


play = 'yes'
mygame = game()
#time.sleep(2)

play = input('Hi {}! Would you like to play a round? (Yes/ No): '.format(mygame.human.get_name()))

while play == 'yes':
	mygame.conduct_round()
	play = input('Would you like to play again? (Yes/ No): ').lower()

mygame.end_game()