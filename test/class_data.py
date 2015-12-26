#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textblob import TextBlob
line = ["кот", "собаку", "любит"]
blob = TextBlob(" ".join(line))
res = blob.translate(from_lang="ru", to="en")
print(res.replace(" ", "_"))

