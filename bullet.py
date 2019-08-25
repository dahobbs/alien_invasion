import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self,ai_settings,screen,ship):
        """Create a bullet object at the ships current position"""
        # inheritance from Sprite
        # when you use sprites you can group releted elements
        # at once to create a bullet instance __init__ needs
        #the ai settings, screen, and ship instances and we call
        #super to iniherit properly from sprite

        super(Bullet,self).__init__()
        self.screen = screen

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
        ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullets position as a decimal number
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
