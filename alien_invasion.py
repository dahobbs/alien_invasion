import sys
import pygame

from settings import Settings
from ship import Ship

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
    ship = Ship(screen)


    #start the main loop for the run_game
    while True:

        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw the screen during each pass of the loop
        screen.fill(bg_color)
        ship.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()
run_game()
