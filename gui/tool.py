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

        self.button = {}

    @staticmethod
    def get_full_path(icon_dir, icon_name, ext):
        return os.path.join(icon_dir, icon_name + ext)

    def add_buttons(self, *names):
        for but in names:
            if isinstance(but, int):
                self.box.addSpacing(but)
                continue
            lst = but.split('|')
            but = lst[0]

            try:
                auto_repeat = lst[1]
            except IndexError:
                auto_repeat = False


            self.button[but] = templates.ToolButton(self.icon_dir,
                                                    but, self.ext,
                                                    state="enabled")
            if auto_repeat:
                self.button[but].setAutoRepeat(True)

            self.button[but].setStyleSheet(self._button_style)
            self.button[but].setFixedHeight(self.height - 1)
            method_name = but + "_"
            self.button[but].clicked.connect(
                partial(self.press_button, method_name))

            if self.icon_size is not None:
                self.button[but].setIconSize(
                    QtCore.QSize(self.icon_size,
                                     self.icon_size))
            self.box.addWidget(self.button[but])

    def set_button_style(self, style):
        """

        :type style: str
        """
        self._button_style = style

    def press_button(self, name):
        getattr(self.parent, name)()

    def set_icon(self, button_name, icon_name):
        pth = self.get_full_path(self.icon_dir, icon_name, self.ext)
        self.button[button_name].setIcon(QtGui.QIcon(pth))

