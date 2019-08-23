import sys
import pygame

def run_game():
    #initialise game and create screen object
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230,230,230)


    #start the main loop for the run_game
    while True:

        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw the screen during each pass of the loop
        screen.fill(bg_color)

        #make the most recently drawn screen visible
        pygame.display.flip()
run_game()
