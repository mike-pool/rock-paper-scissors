import game_objects
from game_objects import game
import time

import classtest


play = 'yes'
game = game()
#game.initialize_game()
time.sleep(2)

print(game.test)
print(game.test_init)

play = input('Hi {}! Would you like to play a round?', format(game.human.get_name()).lower())

while play == 'yes':
	game.conduct_round()
	play = input('Would you like to play again?').lower()

game.end_game()