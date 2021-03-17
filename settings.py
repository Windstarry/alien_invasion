class Settings():

    def __init__(self):
        
        #设置屏幕参数
        self.screen_width=960
        self.screen_height=640
        self.bg_color=(230,230,230)

        #设置飞船图像位置
        self.ship_image='images/ship.bmp'
        self.ship_limit = 2

        #设置子弹参数
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 6
        #设置外星人参数
        self.alien_image="images/alien.bmp"
        self.fleet_drop_speed = 30
        #设置游戏加速
        self.speedup_scale = 1.1
        self.score_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #游戏相关参数初始化
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.alien_points = 10
        #设置移动方向,1表示右移，-1表示左移
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.alien_points*self.score_scale)
 