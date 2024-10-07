import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group

def run_game():

    pygame.init() #initializes background settings and create a screen object
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#creates a display window of (wt,ht)
    pygame.display.set_caption("Alien Invasion")

    

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        gf.check_events(ai_settings , screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
        gf.update_screen(ai_settings, screen, ship,aliens, bullets)



run_game()