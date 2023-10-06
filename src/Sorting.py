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


def sort(args):
    """
    Take a list of filenames
    open all files, and sort each line by lexical order
    print all lines (from every file) in sorted order
    """
    all_files = []
    for filename in args:
        file = open(filename)
        # store this somewhere or do something with it
        for line in file:
            all_files.append(line)
        file.close()
    # take lines from every file and sort them
    all_files.sort()
    for i in range(len(all_files)):
        print(all_files[i], end="")
