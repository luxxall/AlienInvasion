import sys, pygame

class AlienInvasion:
    """Basic class to manage game resources and basic settings"""

    def __init__(self):
        """Initialize game and its resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')