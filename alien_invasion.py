import pygame
from settings import Settings
from ship import Ship
# from viking import Viking
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

    # Make a viking:
    # viking = Viking(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Make a group to hold vikings in:
    vikings = Group()

    # Create an army of vikings:
    gf.create_army(ai_settings, screen, vikings)

    # Set the background color:
    bg_color = (0, 102, 153)

    # Start the main loop fo rthe game
    while True:

        # ai_settings, screen, and bullets have been added as arguments here.
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        gf.update_bullets(bullets)

        # print(len(bullets)) # This prints out the number of bullets on screen in the terminal
        gf.update_screen(ai_settings, screen, ship, vikings, bullets)
        # gf.update_screen(ai_settings, screen, ship)

run_game()
