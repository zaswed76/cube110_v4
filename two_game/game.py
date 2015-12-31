#!/usr/bin/env python
# -*- coding: utf-8 -*-

from two_game import level_models as levels

DEFAULT_START_LEVEL_ID = -1

class Game:

    def __init__(self, data_levels, level_id=DEFAULT_START_LEVEL_ID):
        self._level_id = level_id
        self._data_levels = data_levels
        self._count_levels = len(self._data_levels)
        self._current_level = None

    @property
    def level_id(self):
        return self._level_id

    @level_id.setter
    def level_id(self, id):
        self._level_id = id

    @property
    def count_levels(self):
        return self._count_levels

    @property
    def current_level(self):
        return self._current_level

    def increase_level_id(self):
        if self.level_id + 1 != self.count_levels:
            self._level_id += 1

    def decrease_level_id(self):
        if self.level_id != DEFAULT_START_LEVEL_ID + 1:
            self._level_id -= 1

    def create_next_level(self):
        level = self._data_levels[self.level_id]
        self._current_level = getattr(
            levels, level.name)(level)


    def set_data_level(self, data_levels):
        self._data_levels.update(data_levels)

class OneGameWindow(Game):
    def __init__(self, data_levels, level_id=DEFAULT_START_LEVEL_ID):
        super().__init__(data_levels)
        self._level_id = level_id



if __name__ == '__main__':
    from two_game import data_levels

    game = Game()
    game.set_data_level(data_levels.levels)
    game.set_current_level()
