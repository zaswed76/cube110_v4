#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gui.graphics import ImageItem, Scene


class ImageModel(ImageItem):
    def __init__(self, pixmap, name, parent=None, scene=None):
        """

        :param name:
        :param geometry:
        """
        super().__init__(pixmap, name, parent=None, scene=None)


    def mousePressEvent(self, *args, **kwargs):
        print("!!!!!!!")


class Levels:
    def __init__(self, seq_base_pixmap, seq_secondary_pixmap,
                 seq_base_names, seq_secondary_names):
        """

        :param seq_base_pixmap: list-of-QPixmap
        :param seq_secondary_pixmap: list-of-QPixmap
        :param seq_base_names: list-of-str
        :param seq_secondary_names: list-of-str
        """
        self.seq_base_pixmap = seq_base_pixmap
        self.seq_secondary_pixmap = seq_secondary_pixmap
        self.seq_base_names = seq_base_names
        self.seq_secondary_names = seq_secondary_names
        self._base_img_objects = self._get_image_object(
            self.seq_base_pixmap,
            self.seq_base_names)
        self._secondary_img_objects = self._get_image_object(
            self.seq_secondary_pixmap,
            self.seq_secondary_names)

    def _get_image_object(self, pixmaps_list, names):
        """

        :param pixmaps_list: list-of-QPixmap
        :param names: list-of-str
        :return: list-of-ImageModel < ImageItem < QtGui.QGraphicsPixmapItem
        """
        lst = []
        for pxm, name in zip(pixmaps_list, names):
            obj = ImageModel(pxm, name, self, Scene)
            lst.append(obj)
        return lst

    def seq_base(self):
        raise Exception("надо переопределить")


class RememberLevel(Levels):
    def __init__(self, seq_base_pixmap, seq_secondary_pixmap,
                 seq_base_names, seq_secondary_names):
        super().__init__(seq_base_pixmap, seq_secondary_pixmap,
                         seq_base_names, seq_secondary_names)

    @property
    def base_img_objects(self):
        # список объектов ImageModel
        return self._base_img_objects

    def remember(self):
        pass

    @property
    def secondary_img_objects(self):
        # список объектов ImageModel
        return self._secondary_img_objects

    def press_object(self, name_image):
        return


if __name__ == '__main__':
    remember = RememberLevel(['1', '2'], [])
    print(remember.seq_base)
