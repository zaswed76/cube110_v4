#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join
from collections import OrderedDict
import json


class _Level:
    def __init__(self, image_dir,
                 base_seq, level_name, info_name,
                 secondary_seq=None):
        self.base_seq = map(str, base_seq)
        if secondary_seq is None:
            self.secondary_seq = []
        else:
            self.secondary_seq = map(str, secondary_seq)
        self.level_name = level_name
        self.info_name = info_name
        self.base_paths = self.get_paths(image_dir, self.base_seq)
        self.secondary_paths = self.get_paths(image_dir,
                                              self.secondary_seq)

    @staticmethod
    def get_paths(idir, seq):
        if seq is not None:
            return [join(idir, n) for n in seq]
        else:
            return []

    def __repr__(self):
        return '''
        ______________________________________________________________
        name: < {} >;
        base_seq: < {} >;
        sec_seq: < {} >;
        info: < {} >
        '''.format(self.level_name, self.base_seq, self.secondary_seq,
                   self.info_name)


class Levels(OrderedDict):
    def __init__(self, data_levels_path, image_dir):
        super().__init__()
        self.image_dir = image_dir
        self.data_levels_path = data_levels_path
        self.create_levels()

    @property
    def _get_data(self):
        with open(self.data_levels_path, "r") as obj:
            return json.load(obj)

    def create_levels(self):
        self.update({n: _Level(self.image_dir, *lev) for n, lev in
                     enumerate(self._get_data)})


if __name__ == '__main__':
    path = r"E:\serg\Projects\projects\cube110_v4\data\edit_levels.json"
    idir = r"E:\serg\Projects\projects\all_cubes\resources\image"
    l = Levels(path, idir)
    print(l[0])
