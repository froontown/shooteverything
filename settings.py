class Settings():
    """A class to store all settings for shoot everything."""

    def __init__(self):
        """Inistialize the settings."""
        # Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 102, 153)

        # Ship settings:
        self.ship_speed_factor = 5.5
