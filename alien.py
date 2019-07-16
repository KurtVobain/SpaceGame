import pygame
import os
from random import randint
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        

        #Load the alien image and set its rect atrinute
        self.image_arr = []
        self.image_arr.append(pygame.image.load(os.path.join(os.path.abspath('images'),'alienship.bmp')))
        self.image_arr.append(pygame.image.load(os.path.join(os.path.abspath('images'),'alienship2.bmp')))
        self.image = self.image_arr[randint(0,1)]
        self.rect = self.image.get_rect()
        
        
        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
