import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to manage single alien in fleet"""

    def __init__(self, ai_game):
        """Initialize alien and basic position"""
        super().__init__()
        self.screen = ai_game.screen

        # load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # diplay alien on the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # change position x to float
        self.x = float(self.rect.x)


