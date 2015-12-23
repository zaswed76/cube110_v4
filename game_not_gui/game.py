#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game_not_gui import level_models

class Game:
    _level_id = 0
    def __init__(self, data_levels):
        self.data_levels = data_levels
        self.current_level = None


    @property
    def level_id(self):
        return self._level_id

    def increase_level_id(self):
        self._level_id += 1

    def set_level(self):
        level_line = self.data_levels[self._level_id]
        print(level_line)
        # self.current_level =

if __name__ == '__main__':
    from game_not_gui import data_levels
    game = Game(data_levels.levels)
    game.set_level()