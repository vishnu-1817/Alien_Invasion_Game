class Settings():
    """A class to store all the settings for the game
    
    """

    def __init__(self):

        #screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.ship_speed_factor=1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

