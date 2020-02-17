
import sys

import pygame

from bullet import Bullet
from alien import Alien
#####################################################################

text_color = (256,256,256)

####
def end_game(status = None):
    try:
        sys.exit(status)
    except:
        return
    else: print('Buy!')

####
def draw_text(screen, text, x, y, font, color = None):
    if(color):
        image = font.render(text, True, color)
    else:
        image = font.render(text, True, (0, 0, 0))

    screen.blit(image, (x, y))

####
def active_game_header(game):
    draw_text(
        game.screen, 
        "Ships left: " + str(game.stat.current_ship_count) +
        "Score: " + str(game.stat.current_score), 
        10, 10, game.font)

    #screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

####
def score_header(game):
    draw_text(game.screen, "Game Over", 10, 10, game.font)
    draw_text(game.screen, "N: New game", 20, 30, game.font)
    draw_text(game.screen, "Q: Quit", 20, 50, game.font)
    #text = game.font.render("Game Over", True, (0, 128, 0))
    #game.screen.blit(text, (10, 10))


    #screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

####
def update_screen(game):
    # Redraw the screen during each pass through the loop.
    game.screen.fill(game.settings.bg_color)

    active_game_header(game)
        
    game.ship.update()
    #game.aliens.draw(game.screen)

    for bullet in game.bullets.copy(): #.sprites():
        bullet.update()
        if bullet.rect.bottom <= 0:
            game.bullets.remove(bullet)
    print("bullets: " + str(len(game.bullets)))
    
    collisions = pygame.sprite.groupcollide(game.bullets, game.aliens, True, True)
    game.stat.current_score += len(collisions)*10
    print("aliens: " + str(len(game.aliens)))

    move_aliens(game)
    game.aliens.update()

    if pygame.sprite.spritecollideany(game.ship, game.aliens):
        print("Ship is destroyed!")
        game.stat.game_over(game)

    scr_rect = game.screen.get_rect()
    for alien in game.aliens.sprites():
        if alien.rect.bottom >= scr_rect.bottom:
            print("You failed to protect Earth!")
            game.stat.game_over(game)
            break


    # Make the most recently drawn screen visible.
    pygame.display.flip()

###
def move_aliens(game):
    for alien in game.aliens.sprites():
        if alien.hit_edge():
            change_fleet_direction(game)
            break

####
def change_fleet_direction(game):
    game.settings.fleet_direction *= -1
    for alien in game.aliens.sprites():
        alien.rect.y += game.settings.fleet_drop_speed

####
def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'q'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.bullets.add( Bullet(game) )
            elif event.key == pygame.K_q:
                return 'q'

        game.ship.handle_event(event)
    
    return 'c' # continue execution 


####
def create_fleet(game):
    alien = Alien(game)
    a_width = alien.rect.width
    space_x = game.settings.screen_width - (2 * a_width)
    num_in_row = int(space_x / (2 * a_width))

    a_height = alien.rect.height
    space_y = game.settings.screen_height - (3 * a_height) - game.ship.rect.height
    num_rows = int(space_y / (2*a_height))
    print("num rows: " + str(num_rows) + ", count in row: " + str(num_in_row))

    for y_idx in range(num_rows):
        for x_idx in range(num_in_row):
            alien = Alien(game)
            alien.x = a_width + 2 * a_width * x_idx
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (2*alien.rect.height * y_idx)
            game.aliens.add(alien)

####
def show_score(game):
    game.screen.fill(game.settings.bg_color)
    score_header(game)
    game.button.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'q'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return 'q'

            elif event.key == pygame.K_n:
                return 'n'




