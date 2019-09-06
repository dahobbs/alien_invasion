class GameStats():
    """track statistics for alien invasion"""
    def __init__(self, ai_settings):
        #initialise statistics
        self.ai_settings = ai_settings
        #start alien invasion in an inactive state
        self.game_active = False
        self.reset_stats()
        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        #initialise statistics the can change during the game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
