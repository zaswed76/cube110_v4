#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class Config:
    def __init__(self):
        self.margin = 0

class ToolButton(QtGui.QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.box = QtGui.QVBoxLayout(self)
        self.box.setMargin(0)
        self.box.setSpacing(0)

class Tool(QtGui.QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())