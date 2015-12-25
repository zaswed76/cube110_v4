#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game_not_gui import game, data_levels

class Main:
    game = game.Game(data_levels.levels)

    def __init__(self):
        pass

    def next_show(self):
        self.game.set_current_level()
        left_seq = self.game.current_level.seq_base
        right_seq = self.game.current_level.seq_secondary
        print(left_seq, right_seq, sep=" --- ")


    def left_press(self):
        pass

    def right_press(self):
        pass

    #--------------------------------------------------
    # реакция сцены

    def sceneNone(self, *arg):
        """
        нет изменения сцены
        """
        pass

    def sceneSelect(self, name_scene, name_image):

        """
        выделить елемент
        :param name_image: str
        """
        pass





if __name__ == '__main__':
    main = Main()
    r = None
    while r != "q":
        main.next_show()
        r = input(">>>> ")
