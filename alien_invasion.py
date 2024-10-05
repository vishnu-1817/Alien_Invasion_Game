import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init() #initializes background settings and create a screen object
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#creates a display window of (wt,ht)
    pygame.display.set_caption("Alien Invasion")

    bg_color=(230,230,230)

    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:

        gf.check_events(ai_settings , screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)



run_game()