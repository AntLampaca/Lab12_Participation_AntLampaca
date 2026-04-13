import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load('game_images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint

        self.bullets = pygame.sprite.Group()
        self.max_bullets = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #left
            self.rect.x -= self.speed
        if keys[pygame.K_d]: #right
            self.rect.x += self.speed

    def shoot(self):
        if len(self.bullets) < self.max_bullets:
            bullet = Bullet(self.rect.midtop)
            self.bullets.add(bullet)
        
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self):
        self.get_input()
        self.constraint()
        self.bullets.update()