import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Create bullet in positin of gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.color = 140, 195, 80
        self.speed = 1.3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Transition bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
