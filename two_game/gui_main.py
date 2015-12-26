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
EXT = ".png"
json_file = os.path.join(paths.get_data_dir(),
                             "base_geometry_dict.json")

class LevelDictEmptyError(Exception): pass


class BaseWindow(main_game_seq.BaseWindow):
    _tool_buttons = [10, "next", 805, "help", 10]
    __level_dict = {}

    def __init__(self):
        super().__init__()
        self.base_scene = graphics.Scene(self)
        self.secondary_scene = graphics.Scene(self)
        self.display = graphics.TwoDisplay(self.base_scene,
                                           self.secondary_scene,
                                           size_display)
        self.add_display(self.display)

        self.add_tool()
        self.set_tool_buttons(*self._tool_buttons)

        #-------------------------------------------------------------
        # конвертируем в dict data_levels.levels
        # добавляем в dict list-of-QPixmap
        self._convert_data_lst_to_dict(data_levels.levels)
        self.data_geometry = data.JsonData(json_file)
        self.data_geometry.load()

        self.game = game.Game()
        self.game.set_data_level(self.level_dict())
        self.game.set_data_geometry(self.data_geometry)







    def next_(self):
        self.game.set_current_level()
        left_seq = self.game.current_level.base_img_objects
        right_seq = self.game.current_level.secondary_img_objects
        self.base_scene.add_items(*left_seq)

    def help_(self):
        print("help")

    def level_dict(self):
        if not self.__level_dict:
            raise LevelDictEmptyError(
                "надо вызвать < _convert_data_lst_to_dict >")
        return self.__level_dict

    def _convert_data_lst_to_dict(self, levels_list):
        """
        конвертирует data_levels в словарь; вычисляет полные пути;
        создаёт объкты QPixmap и добавляет в словарь
        :return: None
        """

        def name_to_pxm(name):
            """

            :param name: str имя файла без расширения
            :return:
            """
            path = os.path.join(paths.get_image_dir(), name + EXT)
            if not os.path.isfile(path):
                FileNotFoundError(
                    "файл < {} > не найден ".format(path))
            return QtGui.QPixmap(path)

        for name, level in enumerate(levels_list):
            level_dict = {}
            level_dict["base_names"] = list(map(str, level[0]))
            level_dict["sec_names"] = list(map(str, level[1]))
            level_dict["level_name"] = level[2]
            level_dict["info_name"] = level[3]
            level_dict["base_pxm"] = list(map(name_to_pxm,
                                         level_dict["base_names"]))
            level_dict["sec_pxm"] = list(map(name_to_pxm,
                                        level_dict["sec_names"]))
            self.__level_dict[name] = level_dict



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    main.next_()
    print(main.data_geometry)
    sys.exit(app.exec_())
