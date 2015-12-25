#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from PyQt4 import QtGui
from gui.graphics import ImageItem, Scene


class ImageModel(ImageItem):
    def __init__(self, pixmap, parent=None, scene=None):
        """

        :param name:
        :param geometry:
        """
        super().__init__(pixmap, parent=None, scene=None)




class Levels:
    _actions = []
    _image_dir_path = None

    def __init__(self, image_dir_path, seq_base):
        self._image_dir_path = image_dir_path
        self._seq_base = seq_base

    def set_actions(self, actions_name):
        self._actions.extend(actions_name)

    def seq_base(self):
        raise Exception("надо переопределить")


class RememberLevel(Levels):
    def __init__(self, seq_base, seq_secondary):
        super().__init__(seq_base, seq_secondary)

        self._base_img_objects = self._set_image_object(seq_base)
        self._secondary_img_objects = self._set_image_object(seq_secondary)


    def _set_image_object(self, pixmaps_list):
        lst = []
        for pxm in pixmaps_list:
            obj = ImageModel(pxm, self, Scene)
            lst.append(obj)
        return lst


    @property
    def base_img_objects(self):
        # список объектов ImageModel
        return self._base_img_objects

    @property
    def secondary_img_objects(self):
        # список объектов ImageModel
        return self._secondary_img_objects

    def press_object(self, name_image):
        return


if __name__ == '__main__':
    remember = RememberLevel("dir", ['1', '2'], [])
    print(remember.seq_base)
