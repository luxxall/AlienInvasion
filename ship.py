import pygame

class Ship:
    """Class for ship management"""

    def __init__(self, ai_game):
        """Initialize ship and its start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # every new ship shows at screens bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Display ship at current position"""
        self.screen.blit(self.image, self.rect)