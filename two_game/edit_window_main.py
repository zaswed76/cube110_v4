#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import paths
from PyQt4 import QtGui

from libs import data
from two_game.game import OneGameWindow
from two_game import data_levels as levels
from gui import main_game_seq, graphics, styles, tool

json_file = os.path.join(paths.get_data_dir(),
                         "base_geometry_dict.json")
level_file = os.path.join(paths.get_data_dir(),
                          "edit_levels.json")
settings_file = os.path.join(paths.get_data_dir(),
                             "edit_settings.json")

config = data.JsonData(settings_file)
config.load()

_size_display = config["size_display"]
_scene_geometry = config["scene_geometry"]
_height_tool = config["height_tool"]
_tool_icon_size = config["tool_icon_size"]
_EXT = config["EXT"]
_tool_buttons = config["tool_buttons"]




class BaseWindow(main_game_seq.BaseWindow):
    press_method_name = "press_method"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.image_geometry = data.JsonData(json_file)
        self.image_geometry.load()
        self.scene = graphics.Scene(self, _scene_geometry,
                                    self.press_method_name,
                                    self.image_geometry)
        self.display = graphics.View(_size_display, self.scene, self)
        self.display.setStyleSheet(styles.default_display_css)
        self.add_display(self.display)
        self.tool = tool.ToolBar(parent=self,
                                 icon_dir=paths.get_icon_dir(),
                                 height=_height_tool,
                                 icon_size=_tool_icon_size)
        self.tool.setStyleSheet(styles.tool_css)
        self.tool.set_button_style(styles.tool_button_css)
        self.add_tool(self.tool)
        self.set_tool_buttons(*_tool_buttons)

        self.data_levels = levels.Levels(levels.Level, level_file,
                                         paths.get_image_dir())
        self.game = OneGameWindow(self.data_levels,
                                  level_id=config["start_level_id"])

    def closeEvent(self, event):
        config["start_level_id"] = self.game.level_id - 1
        config.save()

    def set_current_level(self):
        self.game.create_next_level()
        self.scene.set_level(self.game.current_level)


    def press_method(self, name):
        print(name)

    #---- методы панели инструментов --------------------------------

    def prev_(self):
        self.game.decrease_level_id()
        self.set_current_level()

    def next_(self):
        self.game.increase_level_id()
        self.set_current_level()


    def zoom_in_(self):
        self.set_current_level()

    def zoom_out_(self):
        self.scene.zoom()

    def mirror_(self):
        print("mirror")

    def save_(self):
        self.image_geometry.save(self.scene.img_geomety)




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    main.next_()

    sys.exit(app.exec_())
