#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    sum = 0;
    for i in range(1,len(args)):
        sum += int(args[i])
    print("{}".format(sum))
