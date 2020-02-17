import pygame
from pygame.sprite import Group

import engine
from settings import Settings
from ship import Ship
from alien import Alien
from game_stat import Stat
from button import Button
from scoreboard import Scoreboard_screen

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.font = pygame.font.Font(None, 16)
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.scoreboard = Scoreboard_screen(self)

        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()
        self.stat = Stat(self)

        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""

        #engine.create_fleet(self)
        
        #self.stat.new_game(self)

        while True:
            #check_evemts(self)
            if self.stat.game_active:
                action = engine.handle_events(self)
                if action != 'q':
                    engine.update_screen(self)

                if len(self.aliens) == 0:
                    self.stat.new_game(self)

            else:
                action = self.scoreboard.run()
                #engine.show_score(self)

            if action == 'p':
                self.stat.new_game(self)
            elif action == 'q':
                break

        engine.end_game()

##############################################################################
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
