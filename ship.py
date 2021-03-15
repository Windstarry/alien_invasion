import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图形，并获取其外接矩形
        self.image=pygame.image.load(self.ai_settings.ship_image)
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将飞船放于屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom-3
        #设置飞创属性center可以储存小数
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
        #移动标志
        self.moving_right= False
        self.moving_left= False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #根据移动标志调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top >0 :
            self.centery -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        #更新rect的数值
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery
        

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx