import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets"""

    def __init__(self, ai_game):
        """Create bullet at ships location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # create new bullet at 0, 0 location and transfer it to ships top rect point
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # change bullet position to float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet on the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Displays bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)