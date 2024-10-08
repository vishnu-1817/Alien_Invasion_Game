class Settings():
    """A class to store all the settings for the game
    
    """

    def __init__(self):

        #screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (0,0,0)
        # self.ship_speed_factor=1.5

        #bullet settings
        # self.bullet_speed_factor= 10
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 250,250,125
        self.bullets_allowed = 3
        
        #aliens settings
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = -1

        #ship settings
        self.ship_limit= 2
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        #scoring 
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale



