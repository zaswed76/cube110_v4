#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

модуль предоставляет абстрактный класс Data
класс Data предоставляет "интерфейс"  load
который загружает базу из файла

в классе потомке требуется реализация метода get_data

>>> data = JsonData()
>>> data.load("path")

'''

import os
import json
import shelve

class DataError(Exception): pass

_FILE_ASSERT_TEMPLATE = "файл < {} > не существует"
_METHOD_ERROR_ASSERT_TEMPLATE = "метод < {} > надо переопределить в наследнике"


class Data(dict):
    def __init__(self, path):
        """
        в классе потомке требуется реализация метода get_data
        метод должен вернуть dict
        """
        super().__init__()
        self.path = path
        assert hasattr(self, "get_data")

    def load(self):
        if self:
            self.clear()
        if not os.path.isfile(self.path):
            raise FileNotFoundError(
                _FILE_ASSERT_TEMPLATE.format(self.path))

        self.update(self.get_data(self.path))

    def save(self, obj=None, path=None):
        if obj is None:
            obj = self
        if not isinstance(obj, dict):
            raise Exception("obj может быть только dict")
        elif not obj:
            raise Exception("не может быть пуст")
        if path is None:
            path = self.path
        with open(path, "w") as json_obj:
            json.dump(obj, json_obj, indent=2)




class JsonData(Data):
    def get_data(self, path):
        with open(path, "r") as obj:
            return json.load(obj)


class ShelveData(Data):
    def get_data(self, path):
        path = os.path.splitext(path)[0]
        return shelve.open(path)


if __name__ == '__main__':
    import paths
    json_file = os.path.join(paths.get_data_dir(),
                             "base_geometry_dict.json")
    # shelve_file = os.path.join(paths.get_data_dir(), "dict_shl",
    #                            "secondary_geometry_shl.dat")
    #
    #
    def load(path, data_cls):
        data = data_cls()
        data.load(path)
        # print(data)


    load(json_file, JsonData)
    # load(shelve_file, ShelveData)
    # import doctest
    # doctest.testmod()