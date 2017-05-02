import pygame
from pygame.sprite import Sprite

class Viking(Sprite):
    """A class representing a human attacker."""

    def __init__(self, ai_settings, screen):
        """Initialize the viking and set its starting position."""
        super(Viking, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the viking image and set its rect attribute
        self.image = pygame.image.load('images/viking.bmp')
        self.rect = self.image.get_rect()

        # Store the viking's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the viking at its current location."""
        self.screen.blit(self.image, self.rect)
