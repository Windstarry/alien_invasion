from bullet import Bullet
from alien import Alien
import sys
import pygame

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        #print("游戏正在退出中......")
        sys.exit()

def check_keyup_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #print("游戏正在退出中......")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    #更新屏幕上的图像，并切换新屏幕
    screen.fill(ai_settings.bg_color)
    #绘制所有子弹s
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #更新屏幕
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)
        #print(len(bullets))

def fire_bullet(ai_settings,screen,ship,bullets):
    '''
    如果没有达到子弹限制数目，就发射子弹
    创建新子弹，并加入到bullets编组中
    '''
    if len(bullets) < ai_settings.bullet_allowed:
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens):
    """
    创建外星人群，计算一行有多少外星人
    外星人间距为外星人宽度
    """
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)

    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

