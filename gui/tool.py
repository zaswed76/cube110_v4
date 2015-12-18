#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from gui import templates, styles
from functools import partial

class ToolBar(QtGui.QFrame):
    def __init__(self, parent, height):
        super().__init__()
        self.parent = parent
        self.setFixedHeight(height)
        self.box = templates.HBoxLayout(self)

        self.buttons = {}

    def add_buttons(self, *names):
        for but in names:
            self.buttons[but] = templates.ToolButton()
            self.buttons[but].setStyleSheet(styles.tool_button_css)
            self.buttons[but].clicked.connect(partial(self.press_button, but))
            self.buttons[but].setText(but)
            self.box.addWidget(self.buttons[but])




    def press_button(self, name):
        print(name)