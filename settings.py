class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed_factor = 1 #2 #1.5
        self.max_ship_count = 3

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        #alien settings:
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        #fleet_direction of 1 move right; -1 move left
        self.fleet_direction = 1
