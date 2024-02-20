import pygame
from pygame.sprite import Sprite

class Alien (Sprite):
    def __init__(self, ai) -> None:
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings

        self.image = pygame.image.load("resurs/alien.png")
        self.image = pygame.transform.scale(self.image, (60, 35))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x