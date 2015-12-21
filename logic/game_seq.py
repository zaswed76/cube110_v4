#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gui import graphics



class Imagemodel(graphics.ImageItem):
    def __init__(self, pixmap):
        """
        описывает модель изображения
        :param QPixmap pixmap:
        """
        super().__init__(pixmap)


class Step:
    def __init__(self, left_seq, right_seq, game_logic, info):
        """

        :param left_seq: list имена изображений
        :param right_seq: list
        :param game_logic: str имя метода
        :param info: str имя html файла информационного окна
        """
        self._info = info
        self._game_logic = game_logic
        self._right_seq = right_seq
        self._left_seq = left_seq
        # списки заполняются объктами класса Imagemodel
        self._image_objects_left = []
        self._image_objects_right = []

class Game:
    def __init__(self):
        pass

    def get_current_step(self):
        pass