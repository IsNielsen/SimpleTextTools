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


def wc(files):
    """print newline, word, and byte counts for each file"""
    """
        Take a list of filenames
        for each file in the list:
        open the file, count lines, words, and characters
        print lines, words, characters, and filename
    """
    multFile = len(files) > 1  # true if more than 1 file
    total_line, total_word, total_char = 0, 0, 0
    for filename in files:
        char_count, word_count, line_count = 0, 0, 0
        file = open(filename)
        for line in file:
            if "" in line:  # every char
                char_count += 1
            if " " in line:  # check for words
                word_count += 1
            if "\n" in line:  # check for lines
                line_count += 1
        print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")
        total_line += line_count
        total_word += word_count
        total_char += char_count
        file.close()
    if multFile:
        print(f"{total_line}\t{total_word}\t{total_char}\t TOTAL")
