import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    """respond to keypresses and mouse events"""
    #watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """start new game when player clicks play"""
    button_clicked =  play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset game settings
        ai_settings.initilise_dynamic_settings()
        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #empty list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #crete and new fleet and center ship
        ship.center_ship()

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key ==pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings,screen,ship,aliens,bullets):
    bullets.update()

    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    """update position of bullets and get rid of old bullets"""
    #check for any bullets that have hit alien
    #if so get rid of both the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens)==0:
        #destroy existing bullets and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

        ship.center_ship()
        #pause
        sleep(0.5)

def get_number_aliens_x(ai_settings,alien_width):
    """determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width -2 *alien_width
    number_aliens_x = int(available_space_x /(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height, alien_height):
    """determine the number of rows of aliens that fit in the screen"""
    available_space_y = (ai_settings.screen_height - (3* alien_height - ship_height))
    number_rows = int(available_space_y /(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to ine alien witdh
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


    #create the first row of aliens
    for row_number in range(number_rows):
        #create an alien and place it in the row
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number )

def check_fleet_edges(ai_settings,aliens):
    """respond appropriatley if the aliens reach an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """drop the entire fleet and change the fleets direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """respond to the ship being hit by an alien"""
    if stats.ships_left > 0:
        #decrement no of ships
        stats.ships_left -=1

        #empty lists of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        #enable mouse pointer to appear
        pygame.mouse.set_visible(True)
        ## TODO: put a message on screen saying game over

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button):
    #redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_color)

    #draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
        #make the most recently drawn screen visible
        pygame.display.flip()
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def check_aliens_bottom(ai_settings,stats,aliens,ship,screen,bullets):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


def update_aliens(ai_settings,stats,aliens,ship,screen,bullets):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings,aliens)
    check_aliens_bottom(ai_settings,stats,aliens,ship,screen,bullets)
    aliens.update()
    ship.blitme()
    aliens.draw(screen)
    #make the most recently drawn screen visible
    pygame.display.flip()

    if pygame.sprite.spritecollideany(ship,aliens):
        print("ship destroyed!!")
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
