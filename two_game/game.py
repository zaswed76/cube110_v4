#!/usr/bin/env python
# -*- coding: utf-8 -*-

from two_game import level_models as levels



class Game:
    _level_id = 0
    def __init__(self, data_levels):
        self._data_levels = data_levels
        self._current_level = None

    def set_image_dir(self, path):
        self._image_dir_path = path

    @property
    def level_id(self):
        return self._level_id

    @property
    def current_level(self):
        return self._current_level

    def increase_level_id(self):
        self._level_id += 1

    def set_current_level(self):
        level_line = self._data_levels[self._level_id]
        self._current_level = getattr(
            levels, level_line["level_name"])(
            level_line["base_pxm"],
            level_line["sec_pxm"],
            level_line["base_names"],
            level_line["sec_names"]

        )


    def set_data_level(self, data_levels):
        self._data_levels.update(data_levels)

class OneGameWindow(Game):
    def __init__(self, data_levels):
        super().__init__(data_levels)

    def set_current_level(self):
        level_line = self._data_levels[self._level_id]
        self._current_level = getattr(
            levels, level_line["level_name"])(
            level_line["base_pxm"],
            level_line["base_names"],
        )


if __name__ == '__main__':
    from two_game import data_levels

    game = Game()
    game.set_data_level(data_levels.levels)
    game.set_current_level()
