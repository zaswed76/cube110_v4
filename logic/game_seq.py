#!/usr/bin/env python
# -*- coding: utf-8 -*-



from gui import graphics
from libs.data import ShelveData



class Imagemodel(graphics.ImageItem):
    def __init__(self, pixmap):
        """
        описывает модель изображения
        :param QPixmap pixmap:
        """
        super().__init__(pixmap)


class Level:
    def __init__(self, geometry_left_path, geometry_right_path,
                 left_seq, right_seq, game_logic, info):
        """

        :param left_seq: list имена изображений
        :param right_seq: list
        :param game_logic: str имя метода
        :param info: str имя html файла информационного окна
        """

        self._geometry_left_path = geometry_left_path
        self._geometry_right_path = geometry_right_path
        self._info = info
        self._game_logic = game_logic
        self._right_seq = right_seq
        self._left_seq = left_seq
        # списки заполняются объктами класса Imagemodel
        self._image_objects_left = []
        self._image_objects_right = []

        self.left_geometry = ShelveData()
        self.left_geometry.load(self._geometry_left_path)
        self.right_geometry = ShelveData()
        self.right_geometry.load(self._geometry_right_path)



class Game:
    def __init__(self):
        pass

    def get_current_step(self):
        pass

if __name__ == '__main__':
    import paths