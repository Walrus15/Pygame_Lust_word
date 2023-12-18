import pygame
from support import import_folder
from coin import Coin


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos, screen, status):
        super().__init__()
        self.screen = screen
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.19
        self.status = status
        self.status_portal = 'portal'
        self.image = self.animations['portal'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def import_character_assets(self):
        character_path = 'image/finish/'
        self.animations = {'portal': [], 'flower': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status_portal]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_status(self):
        if self.status:
            self.status_portal = 'flower'
        else:
            self.status_portal = 'portal'

    def update(self, x_shift):
        self.animate()
        self.get_status()
        self.rect.x += x_shift
