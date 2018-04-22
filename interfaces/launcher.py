#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 luna <luna@moon>
#
# Distributed under terms of the MIT license.

"""
Allows fast launching of all interfaces detected
"""

import os
import imp
from importlib import import_module

INTERFACE_MAIN = 'interface.py'

def main():
    print(detectInterfaces())
    while True:
        commands = split(lower(input("PLP> ")))
        command = commands[0]
        if ( command == "help" ):
            help()
        elif ( command == "run" ):
            run(commands)
        elif ( command == "runall" ):
            runall()
        else:
            help()

def detectInterfaces():
    interfaces = {}
    for root, dirs, files in os.walk('./'):
        if(root.count('/') == 1 and INTERFACE_MAIN in files):
            interface_name = root.replace('/','')
            print(interface_name  +"/"+INTERFACE_MAIN)
            interfaces[interface_name] = __import__(interface_name
                            +"/"+INTERFACE_MAIN)
    return interfaces


if __name__ == "__main__":
    main()
