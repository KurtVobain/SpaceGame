
import pygame
from pygame.sprite import Group
from Settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #Make a ship
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    #Make an alien
    alien = Alien(ai_settings, screen)
    
    
    
    
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        
        
        
        

run_game()
    