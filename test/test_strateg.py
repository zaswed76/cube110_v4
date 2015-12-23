#!/usr/bin/env python
# -*- coding: utf-8 -*-

import levels as lv

class Game:
    current_level = None
    def __init__(self, levels):

        self.levels = levels
        self.cursor = 0

    def set_level(self, left, right, level):
        self.current_level = getattr(lv, level)(left, right)

    def play(self):
        level_data = self.levels[self.cursor]
        left, right, level = level_data
        self.set_level(left, right, level)
        self.current_level.play()
        self.cursor +=1




if __name__ == '__main__':

    levels = (([1, 2, 3], [1, 2, 3], "LevelSort"),
              ([5, 6, 7], [5, 6, 7]), "LevelRevers")

    game = Game(levels)
    game.play()
