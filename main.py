import sys

from random import randint

from settings import Settings
from ship import Ship
from bullet import Bullet
from alian import Alien
from star import Star

import pygame

class AlianInvasion:
    """class for managing resources and game behavior"""

    def __init__(self):
        """initializes the game and creates game resources"""

        pygame.init()
        self.settings = Settings()

        if self.settings.fullscreen_flag:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("zalupa conia")

        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_stars()
        self._create_fleet()

    def run_game(self):
        """start the main game loop"""

        while True:

            self._check_event()
            self._update_screen()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()


    def _check_event(self):
        #monitor keyboard and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.ship.muving_right = True
        elif event.key == pygame.K_a:
            self.ship.muving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.muving_right = False
        elif event.key == pygame.K_a:
            self.ship.muving_left = False

    def _create_stars(self):
        for _ in range(self.settings.sum_stars):
            star = Star(self)
            star.rect.x, star.rect.y = randint(0, self.settings.screen_width), randint(0, self.settings.screen_height)
            self.stars.add(star)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height= alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * ship_height)

        for row_number in range (number_rows):
            for alien_number in range (number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height= alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        self.aliens.update()
                
    def _update_screen(self):
        #display the last drawn screen

        self.screen.fill(self.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.stars.draw(self.screen)
        self.aliens.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":

    ai = AlianInvasion()
    ai.run_game()
