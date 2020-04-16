import game_objects.py

play = 'yes'
game = game()
time.sleep(2)

while play == 'yes'
	game.conduct_round()
	play == input('Would you like to play again?').lower()

game.end_game()