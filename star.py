import pygame
from pygame.sprite import Sprite

class Star (Sprite):
    def __init__(self, ai) -> None:
        super().__init__()
        self.screen = ai.screen

        self.image = pygame.image.load("resurs/star.png")
        self.image = pygame.transform.scale(self.image, (10,7))
        self.rect = self.image.get_rect()
