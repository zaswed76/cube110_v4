#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from gui import templates
from gui import styles


def pass_press_method(**kwargs):
    pass


class ImageItem(QtGui.QGraphicsPixmapItem):
    rotate_mod = 3
    scale_mod = 0.005
    Act_rotate = "set_rotate"
    Act_increase = "set_scale_increase"
    Act_decrease = "set_scale_decrease"
    Act_mirror = "mirror"
    def __init__(self, pixmap, name, parent=None, scene=None,
                 geometry=None, press_method_name=None):
        super().__init__()
        self._geometry = geometry
        self._name = name
        self._parent = parent
        self._scene = scene
        self._pixmap = pixmap
        self._main_press_method = press_method_name

        self.setTransformationMode(
                QtCore.Qt.SmoothTransformation)
        self.setPixmap(self._pixmap)
        self.move_start()
        self.allow_edit()

    def mousePressEvent(self, event):
        if self._main_press_method is not None:
            getattr(self._parent, self._main_press_method)(self._name)

    def set_main_press_method(self, method):
        self._main_press_method = method

    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        self._geometry = geometry

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

    def update_position(self):
        self.setPos(self.geometry['x'], self.geometry['y'])
        self.setScale(self.geometry['scale'])
        self.setRotation(self.geometry['rotate'])
        if self.geometry['mirror']:
            self.scale(-1, 1)


    def update_geometry(self):
        self.geometry['x'] = self.pos().x()
        self.geometry['y'] = self.pos().y()
        self.geometry['scale'] = self.scale()


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
        self.geometry['rotate'] += mod
        self.setRotation(self.geometry['rotate'])

    def set_scale_increase(self, **kwargs):
        self.geometry['scale'] += self.scale_mod
        self.setScale(self.geometry['scale'])

    def set_scale_decrease(self, **kwargs):
        self.geometry['scale'] -= self.scale_mod
        self.setScale(self.geometry['scale'])

    def mirror(self):
        self.prepareGeometryChange()
        self.scale(-1, 1)
        if not self.geometry['mirror']:
            self.moveBy(self.get_pixmap_size, 0)
            self.geometry['mirror'] = not self.geometry['mirror']
        else:
            self.moveBy(-self.get_pixmap_size, 0)
            self.geometry['mirror'] = not self.geometry['mirror']

    def allow_edit(self):
        self.setFlags(
            QtGui.QGraphicsItem.ItemIsMovable | \
            QtGui.QGraphicsItem.ItemIsSelectable)


class View(QtGui.QGraphicsView):
    def __init__(self, size, scene, parent, *__args):
        super().__init__(*__args)
        self.setFixedSize(*size)
        self.setScene(scene)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)


class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent, scene_geometry, main_method_press,
                 img_geomety):
        super().__init__()
        self._img_geomety = img_geomety
        self.parent = parent
        self.main_method_press = main_method_press
        self.setSceneRect(*scene_geometry)


    def set_level(self, level):
        if self.items():
            self.clear()
        for name, path in level:
            pixmap = QtGui.QPixmap(path)
            item = ImageItem(pixmap, name, self.parent, self,
                             press_method_name=self.main_method_press)
            self.addItem(item)
            item.geometry = self._img_geomety[name]
            item.update_position()


    @property
    def img_geomety(self):
        self.update_items_geometry()
        return self._img_geomety

    def update_items_geometry(self):
        for item in self.items():
            item.update_geometry()

    @img_geomety.setter
    def img_geomety(self, data):
        self._img_geomety = data

    def selected_items(self):
        pass
        # print(self.selectedItems())

    def zoom(self):
        for item in self.selectedItems():
            item.set_scale_increase()


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
