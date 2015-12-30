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
    def __init__(self, **kwargs):
        """
        __init__(graphics.Scene base_scene=None,
         graphics.Scene secondary_scene=None, QWidget display=None)
        """
        super().__init__()
        self.tool = None
        self.box = templates.VBoxLayout(self)

    def add_display(self, display):
        """

        :param display: QWidget
        """
        self.box.addWidget(display)

    def add_tool(self, tool_bar, height_tool=height_tool,
                 styles=styles.tool_css, icon_size=tool_icon_size,
                 icon_dir=paths.get_icon_dir()):
        self.tool = tool_bar
        self.box.addWidget(self.tool)

    def set_tool_buttons(self, *args):
        """

        :param args: int = пустота в пикселях
                     str = имя иконки без расширенияенн
                     затем надо определить в классе
        родителе метод с < именем + _>
        """
        self.tool.add_buttons(*args)




class BaseController(BaseWindow):
    def __init__(self):
        super().__init__()
        self.step = None

    def next_(self):
        print("next")

    def help_(self):
        print("help")

    def set_step(self, step):
        self.step = step


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
