#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

import sys
from Usage import usage

def cut(args):
    """
    Take a list of args
    check for modifiers that will change what column is being printed
    for each file, print the specified column
    """
    column_to_cut = []  # default

    if len(args) == 0:
        usage()
        sys.exit(1)
    # if there is a modifier and there is at least 3 args
    if args[0] == "-f":
        if len(args) >= 3: # and args[1].isdigit():
            temp = args[1].split(",")
            for i in range(len(temp)):
                column_to_cut.append(int(temp[i]))
            #print(column_to_cut)
            args.pop(0)
            args.pop(0)
        else:
            print("Not enough arguments given")
            sys.exit(1)
    else:
        column_to_cut.append(1)
    # should be left with only file names as arguments now
    for filename in args:
        file = open(filename)
        # split file into columns separated by `,`
        for line in file:
            temp = []
            for i in column_to_cut:
                #temp.join(line.split(",")[i-1])
                #print(line.split(",")[i-1])
                temp.append(line.split(",")[i-1].strip())
            print(",".join(temp))
                #print(",".join(temp))
        # print the column specified by `column_to_cut - 1`


def paste(args):
    """merge lines of files"""
    print("TODO: merge lines of files")
