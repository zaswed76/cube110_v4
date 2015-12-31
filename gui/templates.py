#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

_margin = 0
_spacing = 0


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
    def __init__(self, *__args):
        super().__init__(*__args)
        # self.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

