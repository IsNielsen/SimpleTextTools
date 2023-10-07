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


def grep(args):
    """
    Take list of args
    If first arg is `-v`: invert grep
    else: next arg is the pattern to look for.
    for each file in filenames
    open, search for pattern, print words with(-v: without) pattern.
    """
    if len(args) == 0:
        usage("Please provide a pattern and at least one filename", tool="grep")
        sys.exit()
    # preg = true implies that -v has been called
    preg = False
    if args[0] == "-v":
        preg = True
        if len(args) < 2 or type(args[1]) != str:
            usage("Please provide a pattern and at least one filename", tool="grep")
            sys.exit()
        args.pop(0)
    if len(args) <= 1:
        usage("Please provide a pattern and at least one filename", tool="grep")
        sys.exit()
    pattern = args[0]
    args.pop(0)


    multfile = "" # empty string if there's only one file

    for filename in args:
        file = open(filename)
        if len(args) > 1:
            multfile = f"{filename}:"
        for word in file:
            if not preg and pattern in word:
                print(multfile + word, end="")
            elif preg and pattern not in word:
                print(multfile + word, end="")
        file.close()
