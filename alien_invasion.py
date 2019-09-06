import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #initialise game and create screen object
    pygame.init()
    #instantiate settings object ai for alien invasion

    ai_settings = Settings()

    #screen height and width set in settings.py
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    bg_color = (ai_settings.bg_color)

    #make the play button
    play_button = Button(ai_settings, screen , "Play")
    #make a Ship
    ship = Ship(ai_settings,screen)
    #make a group to store bullets if __name__ == '__main__':
    bullets = Group()
    #make a group of aliens
    aliens = Group()
    #create an instance to store game statistics
    stats = GameStats(ai_settings)

    #create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)



    #start the main loop for the run_game
    while True:

        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,aliens,ship,screen,bullets)

        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)
run_game()
