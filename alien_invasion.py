import sys
import pygame

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("shoot everything")

    # Start the main loop fo rthe game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most reently drawn screen visible:
        pygame.display.flip()

run_game()
