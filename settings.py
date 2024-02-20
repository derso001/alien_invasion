class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (6, 16, 33)
        self.fullscreen_flag = True

        #star settings
        self.sum_stars = 100

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #ship settings
        self.ship_speed = 1

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.5
        self.bullet_color = (166, 5, 5)
        self.bullet_allowed = 3