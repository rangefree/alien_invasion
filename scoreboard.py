import pygame
from button import Button

class Scoreboard_screen(object):
    def __init__(self, game):
        self.screen = game.screen
        self.bg_colotr = game.settings.bg_color
        
        self.best_score = 0
        self.play_button = Button(
            self.screen, 
            pygame.Rect(100,100, 100, 50), 
            (255,0,0),
            (0,0,0),
            "Play", 48)

        self.quit_button = Button(
            self.screen, 
            pygame.Rect(400,100, 100, 50), 
            (255,0,0),
            (0,0,0),
            "Quit", 48)



    def draw(self):
        self.play_button.draw()
        #self.quit_button().draw()

    def run(self):
        #self.screen.fill(game.settings.bg_color)
        self.draw()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'q'
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return 'q'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.play_button.rect.collidepoint(mouse_x, mouse_y):
                        return 'p'
                    elif self.quit_button.rect.collideppoint(mouse_x, mouse_y):
                        return 'q'

