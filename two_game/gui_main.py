#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui
import paths
from libs import data
from gui import main_game_seq, graphics
from two_game import game, data_levels

size_display = (602, 602)
scene_geometry = (0, 0, 600, 600)
EXT = ".png"
json_file = os.path.join(paths.get_data_dir(),
                         "base_geometry_dict.json")


class LevelDictEmptyError(Exception): pass


class BaseWindow(main_game_seq.BaseWindow):
    _tool_buttons = [10, "next", 805, "help", 10]
    __level_dict = {}

    def __init__(self):
        super().__init__()
        self.base_scene = graphics.Scene(self, scene_geometry,
                                         self.graphic_item_press)
        self.secondary_scene = graphics.Scene(self, scene_geometry,
                                              self.graphic_item_press)
        self.display = graphics.TwoDisplay(self.base_scene,
                                           self.secondary_scene,
                                           size_display)
        self.add_display(self.display)

        self.add_tool()
        self.set_tool_buttons(*self._tool_buttons)

        # -------------------------------------------------------------
        # конвертируем в dict data_levels.levels
        # добавляем в dict list-of-QPixmap
        self._convert_data_lst_to_dict(data_levels.levels)

        self.base_geometry = data.JsonData(json_file)
        self.base_geometry.load()
        self.base_scene.set_geometry(self.base_geometry)

        self.game = game.Game(self.level_dict)

    def graphic_item_press(self, **kwargs):
        print(kwargs)

    def next_(self):
        self.base_scene.selected_items()

    def help_(self):
        print("help")

    @property
    def level_dict(self):
        if not self.__level_dict:
            raise LevelDictEmptyError(
                    "надо вызвать < _convert_data_lst_to_dict >")
        return self.__level_dict


    def next_image(self):
        self.game.set_current_level()
        left_seq = self.game.current_level.base_img_objects
        right_seq = self.game.current_level.secondary_img_objects
        self.base_scene.add_items(*left_seq)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    main.next_image()
    # print(main.data_geometry)
    sys.exit(app.exec_())
