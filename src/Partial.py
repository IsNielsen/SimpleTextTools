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


def head(args):
    """
    Take a list of args
    check for modifiers to read length
    for each file in the list of filename
    open the file,
    print the first n lines to the screen with print()
    """

    lines = 10

    if args[0] == '-n':
        lines = int(args[1])
        args.pop(0)
        args.pop(0)     # left with only file names

    for filename in args:
        file = open(filename)  # Just let open() crash if filename is invalid
        if len(args) > 1:
            print(f"\n==> {filename} <==")
        count = 0
        for line in file:
            if count == lines: break
            # print the line, but suppress the extra newline afterward
            print(line, end='')
            count += 1
        file.close()



def tail(args):
    """
    Take a list of args
    check for modifiers to read length
    for each file in the list of filename
    open the file, reverse file
    print last (now technically first) n lines to the screen with print()
    """
    multFile = ""  # empty string if only one file
    lines = 10

    if args[0] == '-n':
        lines = int(args[1])
        args.pop(0)
        args.pop(0)  # left with only file names

    for filename in args:
        file = open(filename)  # Just let open() crash if filename is invalid
        if len(args) > 1:
            print(f"\n==> {filename} <==")
        count = 0
        for line in reversed(list(file)):
            if count == lines: break
            # print the line, but suppress the extra newline afterward
            print(line, end='')
            count += 1
        file.close()
