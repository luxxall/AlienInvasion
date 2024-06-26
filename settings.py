class Settings:
    """Class for all game settings"""

    def __init__(self):
        """Initialize game settings"""
        #game settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        #ship settings
        self.ship_speed = 4
        
        #bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4