import sys, pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game resources and basic settings"""

    def __init__(self):
        """Initialize game and its resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        """Start main game loop"""
        while True:
            # wait for key or mouse to be clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #refresh screen in every loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # display last refreshed screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #create game example and run
    ai = AlienInvasion()
    ai.run_game()