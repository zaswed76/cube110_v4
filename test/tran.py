#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if not sys.argv[1:]:
    print("нет аргументов")
    sys.exit(1)


try:
    file_path = sys.argv[1]
except ValueError:
    print("не указан путь")
    sys.exit(1)

try:
    line = sys.argv[2]
except ValueError:
    print("не указана строка")
    sys.exit(3)

try:
    text_lst = sys.argv[3:]
except ValueError:
    print("нет слов для перевода")
    sys.exit(4)



from textblob import TextBlob
import re

def get_tr_text(text_lst):
    blob = TextBlob(" ".join(text_lst))
    return str(blob.translate(from_lang="ru", to="en"))

class Text(TextBlob):
    def __init__(self, text):
        super().__init__(text)

class ReWriteFile:
    def __init__(self, path, line_num):
        self.line_num = line_num
        self.path = path
        self.lines = []
        self.line = ""

    def set_line_from_file(self):
        with open(self.path, "r", encoding='utf-8') as f:
            self.lines = f.readlines()
            self.line = " ".join(self.lines[int(self.line_num) - 1])

    def set_new_lines(self, old_text, new_text):
        print(self.line)
        line = re.sub(old_text, new_text, self.line)
        self.lines[int(self.line_num) - 1] = line


    def write_lines(self):
        if self.lines is not None:
            with open(self.path, "w", encoding='utf-8') as f:
                f.writelines(self.lines)

if __name__ == '__main__':
    rfile = ReWriteFile(file_path, line)
    rfile.set_line_from_file()
    new = get_tr_text(text_lst)
    rfile.set_new_lines(text_lst, new)
    rfile.write_lines()


