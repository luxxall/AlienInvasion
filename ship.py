import pygame

class Ship:
    """Class for ship management"""

    def __init__(self, ai_game):
        """Initialize ship and its start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # every new ship shows at screens bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # horizontal position stored as float
        self.x = float(self.rect.x)

        # options for ship movement
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update ship movement based on movement option"""
        #move only if ship is within windows borders
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update object position based on float position with ship speed
        self.rect.x = self.x

    def blitme(self):
        """Display ship at current position"""
        self.screen.blit(self.image, self.rect)