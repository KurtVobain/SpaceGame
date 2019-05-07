class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 640
        self.bg_colour = (0, 162, 232)
        
        #Ship settings
        self.ship_speed_factor = 1.5
        
        #Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (250, 60, 60)
        self.bullets_allowed = 3