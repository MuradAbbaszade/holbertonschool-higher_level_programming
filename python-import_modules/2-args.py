#!/usr/bin/python3
if __name__ == "__main__"
    import sys
    args = sys.argv
    if len(args) - 1 == 1:
        print("{} argument.".format(len(args) - 1))
    elif len(args) - 1 == 0:
        print("{} arguments:".format(len(args) - 1))
    else:
        print("{} arguments:".format(len(args) - 1))
    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
