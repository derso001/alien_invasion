import pygame

class Ship():
    """ship control class"""
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("resurs/rocket.png")
        self.image = pygame.transform.scale(self.image, (50, 75))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #saving the real coordinate of the ship
        self.x = float(self.rect.x)

        #movement flags
        self.muving_right = False
        self.muving_left = False



    def update(self):
        if self.muving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.muving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)