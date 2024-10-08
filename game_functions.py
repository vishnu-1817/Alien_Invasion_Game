import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,  screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
               
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings , screen, ship, bullets, stats, play_button, aliens):
    #respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_buttons(ai_settings, screen,stats, play_button,ship, aliens,bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_buttons(ai_settings, screen,stats, play_button,ship, aliens,bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()  
        pygame.mouse.set_visible(False)
        stats.reset_status()
        stats.game_active = True

        aliens.empty()
        bullets.empty()


        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        

def update_screen(ai_settings, screen, ship, aliens, bullets,stats, play_button):
    #updates images on the screen during each pass through the loop

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen) # draw is a in built fn of Group class

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen,ship,  aliens)

def update_bullets(bullets, aliens, ai_settings, screen, ship):
    """update position of bullets and get rid of old bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width    
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien =  Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen,ship,  aliens):
    """creates a full fleet of aliens"""

    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.width, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
        
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break

def change_fleet_direction(ai_settings, aliens):
        for alien in aliens.sprites():
            alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *=  -1

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets):
        check_fleet_edges(ai_settings, aliens)
        aliens.update()

        if (pygame.sprite.spritecollideany(ship, aliens)):
            print("shit hit")
            ship_hit(ai_settings, stats, screen, ship,aliens, bullets)

        check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship,aliens, bullets):

    if stats.ship_left > 0:
        stats.ship_left -= 1 #decrease the ships left
        

        aliens.empty()
        bullets.empty()

        #make new fleet and center the ship
        create_fleet(ai_settings, screen,ship,  aliens)
        ship.center_ship()

        #pause
        sleep(1)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship,aliens, bullets)
            break