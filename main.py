import pygame, sys
from settings import *
from level import Level
from button import Buttons


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((screen_width, screen_height))  # flags = pygame.NOFRAME
        pygame.display.set_caption("Последнее слово")

        pygame.display.set_icon(pygame.image.load('image/icon.png'))

        self.clock = pygame.time.Clock()

        self.l = True
        self.background_level1 = pygame.image.load("image/background/first_level.jpg")
        self.background_level2 = pygame.image.load("image/background/second_level.jpg")
        self.background_menu = pygame.image.load("image/background/third_level.png")
        self.setup_background()

        self.tile_image = pygame.image.load("image/tiles/tile2.png")

        self.level = Level(level1_map, self.screen, self.background_level1, self.tile_image, screen_height, False)
        self.level2 = Level(level2_map, self.screen, self.background_level2, self.tile_image, screen_height, True)

        # Buttons
        self.win_image = Buttons(screen_width / 2 - (928 / 2), 60, 928, 228, "",
                                  "image/text/win.png", "image/text/win.png", "")
        self.name_image = Buttons(screen_width / 2 - (800/2), 50, 800, 264, "",
                                  "image/text/name_game.png", "image/text/name_game.png", "")
        self.start_button = Buttons(screen_width/2-(420/2), 400, 420, 200, "",
                                    "image/buttons/button_play_1.png", "image/buttons/button_play_2.png", "")
        self.exit_button = Buttons(screen_width / 2 - (420 / 2), 650, 420, 200, "",
                                   "image/buttons/button_exit_1.png", "image/buttons/button_exit_2.png", "")
        self.continue_button = Buttons(screen_width / 2 - (369 / 2), 650, 369, 224, "",
                                       "image/buttons/menu_button_1.png", "image/buttons/menu_button_2.png", "")

    def setup_background(self):
        self.background = pygame.transform.scale(self.background_menu, (screen_width, screen_height))

    def buttons(self, image, button):
        for button in [image, self.start_button, button]:
            button.update(self.screen, pygame.mouse.get_pos())

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_hovered:
                print("Нажата кнопка 'Играть'")
                self.level_1()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.exit_button.is_hovered:
                print("Нажата кнопка 'Exit'")
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.continue_button.is_hovered:
                print("Нажата кнопка 'Continue'")
                self.l = True

    def menu(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                self.event(event)

            if self.l == True:
                self.buttons(self.name_image, self.exit_button)
            else:
                self.buttons(self.win_image, self.continue_button)

            pygame.display.update()
            self.clock.tick(60)

    def level_2(self):
        self.l = True
        running = True
        while running:
            if self.level2.horizontal_movement_collision() == False:
                self.l = False
                self.level2.reset_level()
                self.menu()
            self.screen.fill((14, 219, 248))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.level2.run()
            pygame.display.update()
            self.clock.tick(60)

    def level_1(self):
        running = True
        while running:
            if self.level.horizontal_movement_collision() == False:
                self.level.reset_level()
                self.level_2()
            self.screen.fill((14, 219, 248))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.level.run()
            pygame.display.update()
            self.clock.tick(60)


Game().menu()


