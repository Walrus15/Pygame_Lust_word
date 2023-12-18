# P = Игрок
# X = Блок
# С = Монетка
# I = Платформа
# E = Выход
level1_map = [
    "                                 ",
    "      C                          ",
    "   X XX                      X  E",
    "XX                      X X   XXX",
    "  X                   X          ",
    "    X               X            ",
    "      X              X    I      ",
    "         X  X    X  X X      X   ",
    "               X            X XXX",
    "     X XX     X         XX       ",
    "P  X      X X          X  X      ",
    "XXX                  XX    XXXXXX",
]

level2_map = [
    "                                                                                       ",
    " X        X   I  X            XXXXXXXXXX                 X                             ",
    "XP         XX     X                   C X          X  X   X            X  X            ",
    " X       XX  X     X      X  XXXXXXXXXXX          I        X  X  X  X                  ",
    "  XXX   X     X     X  X                        X     XX  X                            ",
    "         X      X    X                            I XX   X                             ",
    "       XX         X                                     X                              ",
    "         X          X                           XXXXXXXX                               ",
    "        X      X XXX                         X                                         ",
    "       X    I                             X                                            ",
    "        XX                             X                                               ",
    "   XXXXX  XX                        X                                                  ",
    "              X                 XX                                                     E",
    "             X                                                                         ",
    "   XXXXXX  X                                                                         XXX",
]


tile_size = 64
screen_width = 1280
screen_height = len(level2_map) * tile_size