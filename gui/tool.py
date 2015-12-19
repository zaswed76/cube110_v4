#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from gui import templates, styles
from functools import partial


class ToolBar(QtGui.QFrame):
    def __init__(self, parent, icon_dir, height, ext=".png"):
        super().__init__()
        self.ext = ext
        self.icon_dir = icon_dir
        self.parent = parent
        self.setFixedHeight(height)
        self.box = templates.HBoxLayout(self)
        self._icon_size = None

        self.buttons = {}

    def add_buttons(self, *names):
        for but in names:
            if isinstance(but, int):
                self.box.addSpacing(but)
                continue
            self.buttons[but] = templates.ToolButton()
            method_name = but + "_"
            self.buttons[but].clicked.connect(
                partial(self.press_button, method_name))
            icon_path = os.path.join(self.icon_dir, but + self.ext)
            if os.path.isfile(icon_path):
                self.buttons[but].setIcon(QtGui.QIcon(icon_path))
                if self._icon_size is not None:
                    self.buttons[but].setIconSize(
                        QtCore.QSize(self._icon_size,
                                     self._icon_size))
            else:
                self.buttons[but].setText(but)
            self.box.addWidget(self.buttons[but])

    def set_icon_size(self, size):
        self._icon_size = size

    def press_button(self, name):
        getattr(self.parent, name)()
