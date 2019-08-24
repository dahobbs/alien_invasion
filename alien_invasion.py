import sys
import pygame

from settings import Settings
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

    #make a Ship
    ship = Ship(ai_settings,screen)


    #start the main loop for the run_game
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
run_game()
