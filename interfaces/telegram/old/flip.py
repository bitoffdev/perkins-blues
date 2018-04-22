#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 luna <luna@moon>
#
# Distributed under terms of the MIT license.

"""

"""

f = open("colorDict.py","r")
w = open("colorDict2.py", "w+")
for line in f:
    worka = line.split('"')
    if(len(worka)==5):
        key = worka[1]
        val = worka[3]
        worka[1] = val
        worka[3] = key
        outstr = ""
        for e in worka:
            if (len(outstr) != 0):
                outstr+='"'
            outstr+=e
        line = outstr
    w.write(line)
f.close()
w.close()
