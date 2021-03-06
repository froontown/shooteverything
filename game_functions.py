import sys
import pygame
from bullet import Bullet
from viking import Viking

def check_events(ai_settings, screen, ship, bullets):
    """Respond to key presses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if the limit hasn't been reached."""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Responds to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, vikings, bullets):
    """Update images onscreen and flip to the new screen."""
    # Redraw the screen during each pass through the loop

    screen.fill(ai_settings.bg_color)

    # Redraw all the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    vikings.draw(screen)

    # Make the most reently drawn screen visible:
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()
    # Get rid of bullets when they disappear
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_vikings_x(ai_settings, viking_width):
    """Determine the number of vikings per row."""
    available_space_x = ai_settings.screen_width - 2 * viking_width
    number_vikings_x = int(available_space_x / (2 * viking_width))
    return number_vikings_x

def create_viking(ai_settings, screen, vikings, viking_number, row_number):
    """Create a viking and place it in the row."""
    viking = Viking(ai_settings, screen)
    viking_width = viking.rect.width
    viking.x = viking_width + 2 * viking_width * viking_number
    viking.rect.x = viking.x
    viking.rect.y = viking.rect.height + 2 * viking.rect.height * row_number
    vikings.add(viking)

def create_army(ai_settings, screen, ship, vikings):
    """Create an army of vikings."""
    # Create a viking and calcluate the number of vikings per row:
    # Space each viking equal to one viking width:
    viking = Viking(ai_settings, screen)
    number_vikings_x = get_number_vikings_x(ai_settings, viking.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, viking.rect.height)

    # Create the army of vikings:
    for row_number in range(number_rows):
        for viking_number in range(number_vikings_x):
            create_viking(ai_settings, screen, vikings, viking_number, row_number)

    # # Create the first row of vikings:
    # for viking_number in range(number_vikings_x):
    #     create_viking(ai_settings, screen, vikings, viking_number)

def get_number_rows(ai_settings, ship_height, viking_height):
    """Determine the number of rows of vikings."""
    available_space_y = (ai_settings.screen_height - (3 * viking_height) - ship_height)
    number_rows = int(available_space_y / (2 * viking_height))
    return number_rows
