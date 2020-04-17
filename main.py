import time

from game_objects import rock_paper_scissors_games
from definitions import UI_wait

play = 'yes'
game = rock_paper_scissors_games()

play = input('Hi {}! Would you like to play a round? (Yes/ No): '.format(game.human.name))
time.sleep(UI_wait)

while play == 'yes':
	game.conduct_round()
	play = input('Would you like to play again? (Yes/ No): ').lower()
	time.sleep(UI_wait)

game.end_game()