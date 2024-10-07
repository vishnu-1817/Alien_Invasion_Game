import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = 0 #self.rect.width
        self.rect.y = 0 #self.rect.height

        #store the alien's exact pos 
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        # print(self.ai_settings.fleet_direction)
        # self.x += (self.ai_settings.alien_speed_factor)
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x





