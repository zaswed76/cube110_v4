#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join as os_join
from PyQt4 import QtGui

_margin = 0
_spacing = 0

def full_path(icon_dir, icon_name, ext):

    path = os_join(icon_dir, icon_name + ext)

    return path

class HBoxLayout(QtGui.QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        self.setMargin(_margin)
        self.setSpacing(_spacing)

class VBoxLayout(QtGui.QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        self.setMargin(_margin)
        self.setSpacing(_spacing)

class ToolButton(QtGui.QPushButton):
    _dir = None
    _ext = ".png"
    def __init__(self, dir, icon_name, ext, state="normal"):
        super().__init__()
        self.state = state
        self.dir = dir
        self.icon_name = icon_name
        self.ext = ext
        self.set_state(self.state)

    def set_state(self, state):
        getattr(self, state)()

    def disabled(self):
        name = "{}{}".format(self.icon_name, self._disabled)
        path = full_path(self.dir, name, self.ext)
        print(path, "p")
        self.setIcon(QtGui.QIcon(path))

    def normal(self):
        self.setIcon(QtGui.QIcon(full_path(self.dir, self.icon_name,
                                           self.ext)))

    def enabled(self):
        name = "{}{}".format(self.icon_name, self._enabled)

        path = full_path(self.dir, name, self.ext)
        print(path, "!!!!!!!")
        self.setIcon(QtGui.QIcon(path))
