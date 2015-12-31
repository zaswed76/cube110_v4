#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join
from collections import OrderedDict
import json

class Level:
    """
        класс - модель для отоборажения одного окна
    """
    def __init__(self, image_dir,
                 base_seq, level_name, info_name):
        """

        :param image_dir:
        :param base_seq:
        :param level_name:
        :param info_name:
        """
        self.base_seq = list(map(str, base_seq))
        self.name = level_name
        self.info_name = info_name
        self.base_paths = self.get_paths(image_dir, self.base_seq)




    @staticmethod
    def get_paths(idir, seq):
        if seq is not None:
            return [join(idir, n) for n in seq]
        else:
            return []

    @staticmethod
    def list_is_full(lst):
        return bool(lst)

    def __repr__(self):
        return '''
        {}    _______________________________________________________
        level_type: < {} >;
        name: < {} >;
        base_seq: < {} >;
        base_paths: < {} >;
        info: < {} >
        '''.format(self.__doc__,
                   self.__class__,
                   self.name,
                   list(self.base_seq),
                   self.list_is_full(self.base_paths),
                   self.info_name)

class LevelTwoWindow(Level):
    def __init__(self, image_dir, base_seq, level_name, info_name,
                 secondary_seq=None):

        super().__init__(image_dir, base_seq, level_name, info_name)
        if secondary_seq is None:
            self.secondary_seq = []
        else:
            self.secondary_seq = map(str, secondary_seq)



        self.secondary_paths = self.get_paths(image_dir,
                                              self.secondary_seq)



    def __repr__(self):
        return '''
        ______________________________________________________________
        name: < {} >;
        base_seq: < {} >;
        base_paths: < {} >;
        sec_seq: < {} >;
        secondary_paths: < {} >;
        info: < {} >
        '''.format(self.name,
                   list(self.base_seq),
                   self.list_is_full(self.base_paths),
                   self.secondary_seq,
                   self.list_is_full(self.secondary_seq),
                   self.info_name)


class Levels(OrderedDict):
    def __init__(self, level_type, data_levels_path, image_dir):
        super().__init__()
        self.level_type = level_type
        self.image_dir = image_dir
        self.data_levels_path = data_levels_path
        self.create_levels()

    @property
    def _get_data(self):
        with open(self.data_levels_path, "r") as obj:
            return json.load(obj)

    def create_levels(self):
        for n, level_line in enumerate(self._get_data):
            level = self.level_type(self.image_dir, *level_line)

            self[n] = level


if __name__ == '__main__':
    path = r"E:\serg\Projects\projects\cube110_v4\data\edit_levels.json"
    idir = r"E:\serg\Projects\projects\all_cubes\resources\image"
    l = Levels(path, idir)
    # print(l[0])
