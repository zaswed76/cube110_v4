#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from gui import templates
from gui import styles


def pass_press_method(**kwargs):
    pass


class ImageItem(QtGui.QGraphicsPixmapItem):
    def __init__(self, pixmap, name, parent=None, scene=None):
        super().__init__()
        self._name = name
        self._parent = parent
        self._scene = scene
        self._pixmap = pixmap
        self.geometry_link = None
        self.geometry_item = dict(x=0,
                                  y=0,
                                  scale=1,
                                  rotate=0,
                                  mirror=False)

        self._main_press_method = pass_press_method


        self.setTransformationMode(
            QtCore.Qt.SmoothTransformation)
        self.setPixmap(self._pixmap)
        self.move_start()
        self.allow_edit()

    def mousePressEvent(self, event):
        self._main_press_method(name=self.name)
    #
    # def mouseReleaseEvent(self, event):
    #     pass
    #     # print()
    #     # print(self.get_geometry())

    def set_main_press_method(self, method):
        self._main_press_method = method

    def set_geometry(self, data):
        self.geometry_link = data
        self.geometry_item = self.geometry_link[self.name]

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name

    @property
    def pixmap(self):
        return self._pixmap

    def draw(self):
        self.setPixmap(self.pixmap)

    def allow_edit(self):
        self.setFlags(
            QtGui.QGraphicsItem.ItemIsMovable | \
            QtGui.QGraphicsItem.ItemIsSelectable)
    #
    # def disable_edit(self):
    #     self.setFlags(QtGui.QGraphicsItem.ItemSendsGeometryChanges)

    def get_geometry(self):
        x, y = self.pos().x(), self.pos().y()
        scale = self.scale()
        rotate = self.geometry_item['rotate']
        mirror = self.geometry_item['mirror']
        # print([x, y], scale, rotate, mirror)

    def restart_geometry(self):
        self.setPos(self.geometry_item['x'], self.geometry_item['y'])
        self.setScale(self.geometry_item['scale'])
        self.setRotation(self.geometry_item['rotate'])
        self._load_mirror()

    def _load_mirror(self):
        if self.geometry_item['mirror']:
            self.scale(-1, 1)

    @property
    def get_pixmap_size(self):
        width = self.pixmap.size().width()
        height = self.pixmap.size().height()
        return max(width, height)

    def move_start(self):
        size = self.get_pixmap_size
        s = size / 2
        self.setTransformOriginPoint(s, s)

    def set_rotate(self, **kwargs):
        delta = kwargs['delta']
        mod = self.rotate_mod
        if delta < 0:
            mod = -mod
        self._rotate += mod
        self.setRotation(self._rotate)

    def set_scale_increase(self, **kwargs):
        self._scale += self.scale_mod
        self.setScale(self._scale)

    def set_scale_decrease(self, **kwargs):
        self._scale -= self.scale_mod
        self.setScale(self._scale)

    def mirror(self):
        self.prepareGeometryChange()
        self.scale(-1, 1)
        if not self._mirror:
            self.moveBy(self.get_pixmap_size, 0)
            self._mirror = not self._mirror
        else:
            self.moveBy(-self.get_pixmap_size, 0)
            self._mirror = not self._mirror


class View(QtGui.QGraphicsView):
    def __init__(self, size, scene, parent, *__args):
        super().__init__(*__args)
        self.setFixedSize(*size)
        self.setScene(scene)
        # self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)



class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent, scene_geometry, main_method_press):
        super().__init__()
        self.main_method_press = main_method_press
        self.setSceneRect(*scene_geometry)
        self.__geometry = {}

    def add_items(self, *items):
        for item in items:
            self.addItem(item)
            item.set_geometry(self.__geometry)
            item.restart_geometry()
            item.set_main_press_method(self.main_method_press)

    def set_geometry(self, data):
        self.__geometry = data
        # print(self.__geometry)

    @property
    def geometry(self):
        return self.__geometry

    def selected_items(self):
        pass
        # print(self.selectedItems())


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
