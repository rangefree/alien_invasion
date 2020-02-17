import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        #2.7 syntax
        #super(Bullet, self).__init__()
        super().__init__()
        self.screen = game.screen

        self.rect = pygame.Rect(
            0, 0, game.settings.bullet_width, 
            game.settings.bullet_height )

        self.rect.centerx = game.ship.rect.centerx
        self.rect.top = game.ship.rect.top

        self.y = float(self.rect.y)
        self.color = game.settings.bullet_color
        self.speed_factor = game.settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




