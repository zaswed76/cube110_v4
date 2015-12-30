#!/usr/bin/env python
# -*- coding: utf-8 -*-

from two_game import level_models as levels


class Game:

    def __init__(self, data_levels):
        self._level_id = 0
        self._data_levels = data_levels
        self._current_level = None

    @property
    def level_id(self):
        return self._level_id

    @property
    def current_level(self):
        return self._current_level

    def increase_level_id(self):
        self._level_id += 1

    def create_next_level(self):
        level = self._data_levels[self._level_id]
        self._current_level = getattr(
            levels, level.name)(level)


    def set_data_level(self, data_levels):
        self._data_levels.update(data_levels)

class OneGameWindow(Game):
    def __init__(self, data_levels):
        super().__init__(data_levels)



if __name__ == '__main__':
    from two_game import data_levels

    game = Game()
    game.set_data_level(data_levels.levels)
    game.set_current_level()
