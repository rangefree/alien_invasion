import pygame
import engine

class Stat(object):
    def __init__(self, game):
        #self.new_game(game)
        self.game_active = False

    def new_game(self, game):
        if not self.game_active:
            self.current_score = 0
            self.game_active = True
            self.current_ship_count = game.settings.max_ship_count
        
        engine.create_fleet(game)
         
    def game_over(self, game):
        game.aliens.empty()
        game.bullets.empty()

        if self.current_ship_count > 0:
            self.current_ship_count -= 1
            print("You have " + str(self.current_ship_count) + " ships left")
            self.new_game(game)
        else:  # self.current_ship_count == 0:
            print("*** Game Over!")
            print("*** Your score: " + str(self.current_score))
            self.game_active = False


