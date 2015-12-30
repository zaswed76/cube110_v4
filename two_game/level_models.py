#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Levels:
    def __init__(self, level):
        self.level = level

    def press_object(self, name_image):
        raise Exception("переопределить надо")


class RememberLevel(Levels):
    def __init__(self, level):
        super().__init__(level)

    def press_object(self, name_image):
        return "RememberLevel"

class EditLevel(Levels):
    def __init__(self, level):
        super().__init__(level)


    def press_object(self, name_image):
        return "EditLevel"



if __name__ == '__main__':
    remember = RememberLevel(['1', '2'], [])
    print(remember.seq_base)
