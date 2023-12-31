import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, sizeX, sizeY, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (sizeX, sizeY))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift