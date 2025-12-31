#!/usr/bin/env python
import re, os

path = "./logs/"
rodneys_library = os.listdir(path)
myString = "60113"
hit_count = 0

for book in rodneys_library:
    file = os.path.join(path, book)
    with open(file, 'r') as inF:
        for index, line in enumerate(inF):
            if myString in line:
                hit_count = hit_count + 1
                print book + "|" + line,


print " \n=> " + str(hit_count)
#text.close()
