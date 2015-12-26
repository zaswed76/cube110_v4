#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import re

arg, path, num_line, enc = sys.argv[1:]
from textblob import TextBlob
blob = TextBlob(arg)
translate_text = str(blob.translate(from_lang="ru", to="en"))

with open(path, "r", encoding='utf-8') as f:
    lines = f.readlines()
    line = lines[int(num_line) - 1]


pat = arg
new = translate_text
new_line = re.sub(pat, new, line)



lines[int(num_line) - 1] = new_line

with open(path, "w", encoding='utf-8') as f:
    f.writelines(lines)
