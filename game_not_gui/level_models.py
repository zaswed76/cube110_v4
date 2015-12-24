#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ImageModel:
    def __init__(self, name, geometry):
        """

        :param name:
        :param geometry:
        """
        self.geometry = geometry
        self.name = name


class Levels:
    _actions = []
    def __init__(self, seq_base):
        self._seq_base = seq_base

    def set_actions(self, actions_name):
        self._actions.extend(actions_name)

    def seq_base(self):
        raise Exception("надо переопределить")


class RememberLevel(Levels):
    def __init__(self, seq_base, seq_secondary):
        super().__init__(seq_base)
        self._seq_base = seq_base
        self._seq_secondary = seq_secondary



    @property
    def seq_base(self):
        # список объектов ImageModel
        return self._seq_base

    @property
    def seq_secondary(self):
        # список объектов ImageModel
        return self._seq_secondary

    def press_object(self, name_image):
        return




if __name__ == '__main__':
    remember = RememberLevel([1, 2], [])
    print(remember.seq_base)
