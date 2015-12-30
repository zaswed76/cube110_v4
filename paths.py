#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

__resource_dir = r"E:\serg\Projects\projects\all_cubes\resources"
# имена каталогова ресурсов
__root = os.path.dirname(__file__)

# ./
__RESOURCE = "resources"
# /
__CSS = "css"
__DATA = "data"

# ./resources
__ICONS = "icons"
__IMAGE = "image"




def get_root():
    return __root

def get_resource_dir():
    resource_dir = os.path.join(os.path.dirname(__root), __RESOURCE)
    if os.path.isdir(resource_dir):
        return resource_dir
    elif os.path.isdir(__resource_dir):
        return __resource_dir
    else:
        raise Exception("не существует каталога \n {}".format(__resource_dir))


def get_icon_dir():
    return os.path.join(get_resource_dir(), __ICONS)


def get_image_dir():
    return os.path.join(get_resource_dir(), __IMAGE)

def get_css_dir():
    return os.path.join(get_root(), __CSS)

def get_data_dir():
    return os.path.join(get_root(), __DATA)



if __name__ == '__main__':
    pass
    # print(get_resource_dir())
