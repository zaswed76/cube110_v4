#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Levels:
    def __init__(self, level):
        self.level = level
        self.data_for_display = list(zip(level.base_seq, level.base_paths))
        self.number_of_items = len(level.base_seq)

    def press_object(self, name_image):
        raise Exception("переопределить надо")

    def __repr__(self):
        return self.level.__repr__()

    def __iter__(self):
        self.id = 0
        return self

    def __next__(self):
        if self.id == self.number_of_items:
            raise StopIteration
        else:
            res = self.data_for_display[self.id]
            self.id += 1
            return res


class RememberLevel(Levels):
    def __init__(self, level):
        super().__init__(level)

    def press_object(self, name_image):
        return "L_pass_method", name_image

class EditLevel(Levels):
    def __init__(self, level):
        super().__init__(level)


    def press_object(self, name_image):
        return "L_pass_method", name_image

class EditContentLevel(Levels):
    def __init__(self, level):
        super().__init__(level)



    def press_object(self, name_image):
        id = self.level.base_seq.index(name_image)
        method = "L_go_to_level"
        return method, id




if __name__ == '__main__':
    remember = RememberLevel(['1', '2'], [])
    print(remember.seq_base)
