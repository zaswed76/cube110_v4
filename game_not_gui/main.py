#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game_not_gui import game, data_levels

class Main:
    data_levels = data_levels.levels
    game = game.Game(data_levels)

    def __init__(self):
        pass

    def next(self):
        self.game.set_level()





if __name__ == '__main__':
    main = Main()
