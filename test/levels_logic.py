#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Levels:
    def __init__(self, seq_left, seq_right):
        self.seq_right = seq_right
        self.seq_left = seq_left

    def game(self):
        raise Exception("надо переопределить")

class LevelSort(Levels):
    def __init__(self, seq_left, seq_right):
        super().__init__(seq_left, seq_right)

    def play(self):
        self.seq_left.sort()
        self.seq_right.sort()
        print(self.seq_left, "111")
        print(self.seq_right, "111")
        print("sort")

class LevelRevers(Levels):
    def __init__(self, seq_left, seq_right):
        super().__init__(seq_left, list)

    def play(self):
        print("revers")

    def increase the counter