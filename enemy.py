import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 800:
            self.kill()