import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("shoot everything")

    # Make a ship:
    ship = Ship(ai_settings, screen)

    # Set the background color:
    bg_color = (0, 102, 153)

    # Start the main loop fo rthe game
    while True:

        # This, along with sys, is now imported and defined in 'game_functions.py'
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
