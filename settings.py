class Settings():

    def __init__(self):
        
        #设置屏幕参数
        self.screen_width=960
        self.screen_height=640
        self.bg_color=(230,230,230)

        #设置飞船图像位置
        self.ship_image='images/ship.bmp'
        self.ship_speed_factor = 1.5

        #设置子弹参数
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 6

        #设置外星人参数
        self.alien_image="images/alien.bmp"
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        #设置移动方向,1表示右移，-1表示左移
        self.fleet_direction = 1