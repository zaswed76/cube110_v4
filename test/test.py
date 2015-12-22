#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class DataJson(dict):
    def __init__(self):
        super().__init__()

    def load(self, path):
        with open(path, "r") as obj:
            self.update(json.load(obj))




class Level:
    def __init__(self, data_obj, path):
        self.data = data_obj()
        self.data.load(path)


if __name__ == '__main__':
    path = "path.json"
    level = Level(DataJson, path)
    print(level.data)


