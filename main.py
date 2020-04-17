from game_objects import game
import time


play = 'yes'
mygame = game()
time.sleep(2)

print(game.test)
print(mygame.test_init)

play = input('Hi {}! Would you like to play a round?', format(mygame.human.get_name()).lower())

while play == 'yes':
	mygame.conduct_round()
	play = input('Would you like to play again?').lower()

mygame.end_game()