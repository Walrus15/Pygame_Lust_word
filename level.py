import pygame
from settings import *
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from player import Player
from coin import Coin
from portal import Portal


class Level:
    def __init__(self, level_data, surface, background_image, tile_image, screen_height, status_portal):
        self.status_portal = status_portal
        self.display_surface = surface
        self.tile_image = tile_image
        self.setup_level(level_data)
        self.level_data = level_data
        self.background_image = background_image
        self.setup_background()
        self.screen_height = screen_height

        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coin = pygame.sprite.GroupSingle()
        self.portal = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size, tile_size, self.tile_image)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'I':
                    tile = Tile((x, y), tile_size, 20, self.tile_image)
                    self.tiles.add(tile)
                if cell == 'C':
                    coin = Coin((x, y), self.display_surface)
                    self.coin.add(coin)
                if cell == 'E':
                    portal = Portal((x, y), self.display_surface, self.status_portal)
                    self.portal.add(portal)

    def setup_background(self):
        self.background = pygame.transform.scale(self.background_image, (screen_width, screen_height))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 2.5

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        coin = self.coin.sprite
        portal = self.portal.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
            # Касание игрока с монетки
            if coin.visible and player.rect.colliderect(coin.rect):
                coin.visible = False
                player.score += 200
            # Касание игрока с порталом
            if player.rect.colliderect(portal.rect):
                return False

    def draw_coin(self):
        coin = self.coin.sprite

        if coin.visible:
            coin.screen.blit(coin.image, coin.rect)

    def draw_portal(self):
        portal = self.portal.sprite

        portal.screen.blit(portal.image, portal.rect)

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.on_ground = True
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ground = False

    def death(self):
        player = self.player.sprite

        if player.rect.y > self.screen_height:
            self.reset_level()

    def reset_level(self):
        self.tiles.empty()
        self.player.empty()
        self.coin.empty()
        self.portal.empty()

        self.setup_level(self.level_data)

        self.display_surface.fill((0, 0, 0))

    def run(self):
        self.display_surface.blit(self.background, (0, 0))

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        self.coin.update(self.world_shift)
        self.draw_coin()

        self.portal.update(self.world_shift)
        self.draw_portal()

        self.death()





