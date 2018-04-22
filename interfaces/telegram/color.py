#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 luna <luna@moon>
#
# Distributed under terms of the MIT license.

"""
Class to represent a color
"""

from colorDict import *

class Color():

    """
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
    """
    def __init__(self, value):
        print(value)
        if ( len(value) == 0 ):
            raise ValueError('Not long enough value')
        if ( value in HexNameDict ):
            value = HexNameDict[value]
        if ( value[0] =='#' or value[0:2] == "0x" ):
            value = value.replace('#', "0x")
            self.red = int(value[0:4], 0)
            self.green = int("0x" + value[4:6], 0)
            self.blue = int("0x" + value[6:8], 0)
        else:
            raise ValueError("Value not understood...")

    def getRed(self):
        return self.red

    def getGreen(self):
        return self.green

    def getBlue(self):
        return self.blue

    def get32bit(self):
        return 65536*self.red + 256*self.green + self.blue

if __name__ == "__main__":
    test = color("blue")
    test2 = color("#1020AA")
    print(test.getRed())
    print(test.getGreen())
    print(test.getBlue())
    print(test2.getRed())
    print(test2.getGreen())
    print(test2.getBlue())
    print(test.get32bit())
    print(test2.get32bit())

