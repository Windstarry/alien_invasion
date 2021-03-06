import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,ai_settings,screen,ship):
        #在飞船所处位置创建子弹位置
        super(Bullet,self).__init__()
        self.screen=screen
        #创建子弹，并设置子弹位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y=float(self.rect.y)
        #设置子弹颜色，速度
        self.color=ai_settings.bullet_color
        self.speed_factor= ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
