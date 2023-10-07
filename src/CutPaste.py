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
        usage("Too few arguments", tool="cut")
        sys.exit(1)
    # if there is a modifier and there is at least 3 args
    if args[0] == "-f":
        if len(args) >= 3: # and args[1].isdigit():
            temp = args[1].split(",")
            for i in range(len(temp)):
                if int(temp[i]) <= 0:
                    usage("A comma-separated field specification is required", tool="cut")
                    sys.exit()
                column_to_cut.append(int(temp[i]))
            #print(column_to_cut)
            args.pop(0)
            args.pop(0)
        else:
            usage("At least one filename is required", tool="cut")
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
                temp.append(line.split(",")[i-1].strip())
            print(",".join(temp))
        file.close()


def paste(args):
    if len(args) == 0:
        usage("Too few arguments", tool="paste")
        sys.exit(1)
    array_of_lines = []
    max_lines = 0
    for filename in args:
        file = open(filename)
        lines = file.readlines()
        max_lines = max(max_lines, len(lines))
        array_of_lines.append(lines)
        file.close()

    # Pad lines with empty strings if necessary
    for lines in array_of_lines:
        while len(lines) < max_lines:
            lines.append("")

    # Join lines with commas and print
    for i in range(max_lines):
        merged_line = ','.join(line[i].strip() for line in array_of_lines)
        print(merged_line)
