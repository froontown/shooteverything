import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("shoot everything")

    # Make a ship:
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Set the background color:
    bg_color = (0, 102, 153)

    # Start the main loop fo rthe game
    while True:

        # ai_settings, screen, and bullets have been added as arguments here.
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        bullets.update()

        # Get rid of bullets when they disappear
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets)) # This prints out the number of bullets on screen in the terminal

        gf.update_screen(ai_settings, screen, ship, bullets)
        # gf.update_screen(ai_settings, screen, ship)

run_game()
