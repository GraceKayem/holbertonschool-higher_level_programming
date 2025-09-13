#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1  # number of arguments (excluding script name)

    word = "argument" if argc == 1 else "arguments"
    end_char = ":" if argc > 0 else "."

    print("{} {}{}".format(argc, word, end_char))

    if argc > 0:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
