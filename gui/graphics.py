#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from gui import templates
from gui import styles

class ImageItem(QtGui.QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None, scene=None):
        super().__init__()
        self.pixmap = pixmap
        self.setPixmap(self.pixmap)

    def mousePressEvent(self, *args, **kwargs):
        print("!!!!!!!")


class View(QtGui.QGraphicsView):
    def __init__(self, size, scene, parent, *__args):
        super().__init__(*__args)
        self.setFixedSize(*size)
        self.setScene(scene)


class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent, *__args):
        super().__init__(*__args)

    def add_items(self, *items):
        for item in items:
            self.addItem(item)



class TwoDisplay(QtGui.QWidget):
    def __init__(self, left_scene, right_scene, size):
        super().__init__()
        self._size = size

        self.box = templates.HBoxLayout(self)
        self.left_scene = left_scene
        self.left = View(self._size, self.left_scene, self)
        self.left.setStyleSheet(styles.left_display_css)

        self.right_scene = right_scene
        self.right = View(self._size, self.right_scene, self)
        self.right.setStyleSheet(styles.right_display_css)

        self.box.addWidget(self.left)
        self.box.addWidget(self.right)