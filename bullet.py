import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship
    """

    def __init__(self, ai_settings, screen, ship):

        """create a bullet obj at the ship's current pos"""
        super(Bullet, self).__init__()
        # super().__init__()
        self.screen = screen

        #create a bullet rect at (0,0) and then set the correct pos
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor



    def update(self):
        self.y -= self.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        



