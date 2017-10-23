#!/usr/bin/env python3
# author: nitepone
"""
Basic command parser to read custom "Perkins Script" files and execute
appropriate commands from the associated adressable RGB strip control library.

:docformat: reStructuredText
"""

import sys
from perkins import *

def main():

    lights = Light()

    if len(sys.argv) < 2:
        filepath = input("Filepath of Perkins Script: ")
    else:
        filepath = sys.argv[1]

    readScript(filepath, lights)


def lineParser(line):
    """
    Parses a line into a set of arguments. Spaces as default delimiter.
    Respects quotations as non delimited strings.

    :param line: A raw line of Perkins Script
    :type line: string
    :return: A list of arguments
    """
    toggleDelimit = False
    stringIndicator = '"'
    delimiter = ' '
    args = []
    argpos = 0

    for cchar in line.strip():
        if cchar == stringIndicator:
            toggleDelimit = not toggleDelimit
        elif cchar == delimiter and not toggleDelimit:
            argpos += 1
        else:
            try:
                args[argpos] += cchar
            except:
                args.append(cchar)
    return args


def executeLine(line, l):
    """
    Executes a string command.

    :param line: A raw line of Perkins Script
    :type line: string
    :return: None
    """
    command = {
        "solid": lambda args, l: l.set_hex(args[1], args[2], args[3]),
        "fade": lambda args, l: l.fade(args[1], args[2], args[3], args[4])
    }
    args = lineParser(line)
    command[args[0]](args, l)
    print(args[0])


def readScript(filepath, lights):
    """
    Reads a Perkins Script file and executes line through line

    :param filepath: Filepath to a Perkins Script file
    :type filepath: string
    :return: None
    """
    with open(filepath, 'r') as f:
        for line in f:
            executeLine(line, lights)


if __name__ == "__main__":
    main()
