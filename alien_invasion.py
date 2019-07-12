
import pygame
from pygame.sprite import Group
from Settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    #Make a ship, a grpup of aliens and a group of bullets
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    pygame.mixer.music.load('sounds/bensound-moose.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)
            

run_game()

input()
    