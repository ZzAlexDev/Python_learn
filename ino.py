import pygame


class Ino(pygame.sprite.Sprite):
    """Class One Ino"""

    def __init__(self, screen):
        """Initialisation and install main posititon"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Draw ino"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move to Gun"""
        self.y += 0.1
        self.rect.y = self.y
