import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('image/food/food.png')
        # self.image.fill((255, 218, 54))
        self.rect = self.image.get_rect(topleft=pos)
        self.visible = True  # видимость монетки

    def update(self, x_shift):
        self.rect.x += x_shift