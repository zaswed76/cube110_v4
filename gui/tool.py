#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from gui import templates, styles
from functools import partial


class ToolBar(QtGui.QFrame):
    def __init__(self, parent=None, icon_dir=None, height=None,
                 icon_size=None, ext=".png"):
        super().__init__()
        self.ext = ext
        self.height = height
        self.icon_dir = icon_dir
        self.parent = parent
        self.setFixedHeight(height)
        self.box = templates.HBoxLayout(self)
        self.icon_size = icon_size
        self._button_style = None

        self.buttons = {}

    def add_buttons(self, *names):
        for but in names:
            if isinstance(but, int):
                self.box.addSpacing(but)
                continue
            self.buttons[but] = templates.ToolButton()

            self.buttons[but].setStyleSheet(self._button_style)
            self.buttons[but].setFixedHeight(self.height-1)
            method_name = but + "_"
            self.buttons[but].clicked.connect(
                partial(self.press_button, method_name))
            icon_path = os.path.join(self.icon_dir, but + self.ext)
            if os.path.isfile(icon_path):
                self.buttons[but].setIcon(QtGui.QIcon(icon_path))
                if self.icon_size is not None:
                    self.buttons[but].setIconSize(
                        QtCore.QSize(self.icon_size,
                                     self.icon_size))
            else:
                self.buttons[but].setText(but)
            self.box.addWidget(self.buttons[but])

    def set_button_style(self, style):
        """

        :type style: str
        """
        self._button_style = style

    def press_button(self, name):
        getattr(self.parent, name)()
