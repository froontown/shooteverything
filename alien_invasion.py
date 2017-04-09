import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("shoot everything")

    # Make a ship:
    ship = Ship(screen)

    # Set the background color:
    bg_color = (0, 102, 153)

    # Start the main loop fo rthe game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most reently drawn screen visible:
        pygame.display.flip()

run_game()
