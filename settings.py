class Settings():
    """A class to store all settings for alien invasion"""
    def __init__(self):
        """initialise the games settings"""
        #screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #alien Settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5

        #How quickly game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point values increase
        self.score_scale = 1.5

        self.initilise_dynamic_settings()
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
    def initilise_dynamic_settings(self):
        """initialisze settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet direction of 1 represents right and -1 represents left
        self.fleet_direction = 1

        #scorekeeping
        self.alien_points = 50
    def increase_speed(self):
        #increase speed Settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
