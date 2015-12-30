#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import paths
from PyQt4 import QtGui, QtCore

from two_game.game import OneGameWindow
from two_game import data_levels as levels
from gui import main_game_seq, graphics, styles, tool

size_display = (604, 604)
scene_geometry = (0, 0, 600, 600)
height_tool = 40
tool_icon_size = 40
EXT = ".png"
json_file = os.path.join(paths.get_data_dir(),
                             "base_geometry_dict.json")
level_file = os.path.join(paths.get_data_dir(),
                          "edit_levels.json")

class BaseWindow(main_game_seq.BaseWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scene = graphics.Scene(self, scene_geometry, self.press_method)
        self.display = graphics.View(size_display, self.scene, self)
        self.display.setStyleSheet(styles.default_display_css)
        self.add_display(self.display)
        self.tool = tool.ToolBar(parent=self,
                                 icon_dir=paths.get_icon_dir(),
                                 height=height_tool,
                                 icon_size=tool_icon_size)
        self.tool.setStyleSheet(styles.tool_css)
        self.tool.set_button_style(styles.tool_button_css)
        self.add_tool(self.tool)
        self.set_tool_buttons("next", "mirror", "save")

        self.data_levels = levels.Levels(level_file, paths.get_image_dir())
        self.game = OneGameWindow(self.data_levels)


    def press_method(self, name):
        print(name)

    def next_(self):
        print('next')

    def save_(self):
        print("save")

    def mirror_(self):
        print("mirror")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())