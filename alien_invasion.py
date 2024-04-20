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
            # check events
            self._check_events()
            self.ship.update()
            
            #refresh screen
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reaction for events from keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reaction for key down"""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
    
    def _check_keyup_events(self, event):
        """Reaction for key up"""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
        elif event.key == pygame.K_q:
             sys.exit()

    def _update_screen(self):
        """"Update screen objects and move to next screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    #create game example and run
    ai = AlienInvasion()
    ai.run_game()