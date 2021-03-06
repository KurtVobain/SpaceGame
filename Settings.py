import pygame
import os
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
        self.ship_limit = 3
        self.ship_lose_sound = pygame.mixer.Sound(os.path.join(os.path.abspath('sound'),'ex5.wav'))
        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.alien_lose_sound =  pygame.mixer.Sound(os.path.join(os.path.abspath('sound'),'ex2.wav'))
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (250, 60, 60)
        self.bullets_allowed = 3
        self.shoot_sound = pygame.mixer.Sound(os.path.join(os.path.abspath('sound'),'las7.wav'))
        self.shoot_sound_2 = pygame.mixer.Sound(os.path.join(os.path.abspath('sound'),'pow2.wav'))