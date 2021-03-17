import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")
    play_button = Button(ai_settings,screen,"PLAY")
    stats=GameStats(ai_settings)
    sb = ScoreBoard(ai_settings,screen,stats)
    ship=Ship(ai_settings,screen)
    aliens=Group()
    bullets=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏循环
    while True:
        
        gf.check_events(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)  
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 



if __name__ == "__main__":
    run_game()