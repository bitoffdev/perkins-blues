#!/usr/bin/env python3
# author: nitepone
"""
Basic command parser to read custom "Perkins Script" files and execute
appropriate commands from the associated adressable RGB strip control library.

:docformat: reStructuredText
"""

def main():
    filepath = input("Filepath of Perkins Script: ")
    readScript(filepath)


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

def executeLine(line):
    """
    Executes a string command.

    :param line: A raw line of Perkins Script
    :type line: string
    :return: None
    """
    args = lineParser(line)
    print(args[0])


def readScript(filepath):
    """
    Reads a Perkins Script file and executes line through line

    :param filepath: Filepath to a Perkins Script file
    :type filepath: string
    :return: None
    """
    with open(filepath, 'r') as f:
        for line in f:
            executeLine(line)


if __name__ == "__main__":
    main()
