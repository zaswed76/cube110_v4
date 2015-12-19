#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import paths
from gui import graphics as gui
from gui import templates, styles, tool

from PyQt4 import QtGui

size_display = (602, 602)
height_tool = 35
tool_icon_size = 28


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.left_model = gui.Scene(self)
        self.right_model = gui.Scene(self)
        self.game_display = gui.TwoDisplay(self.left_model,
                                           self.right_model,
                                           size_display)
        self.tool = tool.ToolBar(self, paths.get_icon_dir(),
                                 height_tool)
        self.tool.setStyleSheet(styles.tool_css)
        self.tool.set_icon_size(tool_icon_size)
        self.box = templates.VBoxLayout(self)
        self.box.addWidget(self.game_display)
        self.box.addWidget(self.tool)

        self._tool_buttons = [10, "next", 805, "help"]

        self.tool.add_buttons(*self._tool_buttons)


class BaseController(BaseWindow):
    def __init__(self):
        super().__init__()

    def next_(self):
        print("next")

    def help_(self):
        print("help")


if __name__ == '__main__':
    css_path = os.path.join(paths.get_css_dir(), "base.css")
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open(css_path, "r").read())
    main = BaseController()
    main.show()
    img = os.path.join(paths.get_image_dir(), "1.png")
    pxm = QtGui.QPixmap(img)
    item = gui.ImageItem(pxm, scene=main.left_model)
    main.left_model.draw(item)




    sys.exit(app.exec_())