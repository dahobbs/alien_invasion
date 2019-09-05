class GameStats():
    """track statistics for alien invasion"""
    def __init__(self, ai_settings):
        #initialise statistics
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        #initialise statistics the can change during the game
        self.ships_left = self.ai_settings.ship_limit
