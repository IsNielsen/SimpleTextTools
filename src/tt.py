#!/usr/bin/env python

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

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    # print("TODO: Determine which tool the user has invoked by examining sys.argv")
    # print("TODO: Use if/elif/else to select which function to call")
    # print("TODO: Call the requested tool, passing remaining arguments from sys.argv")
    # print("TODO: Call usage() and exit when bad input is provided")
    print("this printed")
    tool = sys.argv[1]
    print(tool)
    list_of_args = sys.argv[2:]  # get rid of tool from array before passing into function
    if tool == "cat":
        cat(list_of_args)
    elif tool == "tac":
        tac(list_of_args)
    elif tool == "grep":
        grep(list_of_args)
    elif tool == "head":
        head(list_of_args)
    elif tool == "wc":
        wc(list_of_args)
    elif tool == "sort":
        sort(list_of_args)
    elif tool == "tail":
        tail(list_of_args)
    elif tool == "cut":
        cut(list_of_args)
    elif tool == "paste":
        paste(list_of_args)
    else:
        usage()
        sys.exit(1)

