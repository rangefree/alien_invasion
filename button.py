import pygame
import pygame.font

class Button(object):
    def __init__(self, screen, rect, bg_c, txt_c, text, font_size):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = rect
        self.bg_color = bg_c
        self.txt_color = txt_c
        self.font = pygame.font.SysFont(None, font_size)

        self.txt_image = self.font.render(text, True, self.txt_color, self.bg_color)
        self.txt_image_rect = self.txt_image.get_rect()

        #adjust button width to hold text:
        self.rect.width = self.txt_image_rect.width

        self.txt_image_rect.center = self.rect.center


    def draw(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.txt_image, self.txt_image_rect)