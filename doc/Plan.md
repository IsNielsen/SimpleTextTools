# Software Development Plan

## Phase 0: Requirements Analysis
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).

### Cat tool

Create a Python function that will accept *command line arguments* which name files.  I will *open the files* and *read their contents* and print the lines to the console.

If multiple files are named, read and print their contents in the order they show up on the command line

*   Things I know how to do
    * print text to the screen using `print()`

* Things I don't know how to do
    * Command line arguments
    * Open files
    * Read files

* data used by the program
    * The strings on the command line
    * The data inside the files

The Output will appear through the `print()` function as one long file that is the concatenation of each input file

No algorithms; I'm just copying data from files to the screen.

### grep tool

Create a Pythong funcion that accepts *command line args*, an optional modifier, a string to look for, and file names. *Open file* and *read content* and print all words containing pattern string.

If multiple files, print the found words with name of file *FILENAME:pattern*

*   Things i know:
    * `print()`
    * open files

*   Things I dont know:
    * split/take only certain words from a file

*   Data used:
    * Strings on command line
    * data in files
    * can I use arrays/lists?

Output through the print tool with one word per line

Algorithms: in-order search through file, finding pattern in words.

### head tool

Create a python function that accepts *command line args*, an optional modifier, a digit (n), and file name(s). Open file and read first n lines (n<=10 by defailt)

If multiple files, print `==> FILENAME <==` then the top `n` lines of the file (then repeat).

*   what I know:
    * how cat works, to read and print the file

*   What I dont know:
    * I think Im good? Wish me luck

*   Data needed:
    * commandline inputs, 
    * Files, modifier(flag)
*   Algorithms:
    * Loop over files (for loop)
    * Error handling through usage()

### wc tool

Create a function that accepts *command line args* that name files. Read through file(s) and count number of lines, words, and characters.
If multiple files, print each files output like normal, and then print a total count after.

*   What I know:
    * how to read a file and look for certain patterns
    * everything i knew from above tools

*   What I dont know:
    * How to allign the output
    * What the character and newline patters might be
         * is character just "" and newline "/n"?
*   Algorithms:
    * Loop over files (for loop)
    * Error handling through usage()

### sort tool

Create a function that accepts *command line args* as file name(s). Open and read files, and then sort the lines by lexical order and print.

If there are multiple files, everything is sorted together in one big string.

*   What I know:
    * Spaces `(" ")` are counted as character, and have a higher priority than letters
        * Therefore, empty lines are printed first, then any lines with indentations.
    * I can read a line of a file and look for certain elements
*   What I don't know:
    * How the heck ASCII characters work
    * How to sort by ASCII

*   Data needed:
    * Each file that is called
    * Might need an array that contains lines from every file, then sort that.

*   Algorithms:
    * Loop over files (for loop)
    * Error handling through usage()

### tac tool
Similar to cat, but instead this function will print the lines of the file in reverse order
If multiple files, do it for each file in turn

*   What I know:
    * how cat works
    * read and print file
*   What I dont know:
    * how to iterate through the file backward
*   Data needed:
    *  Input from commandline arguments
    * Files 
  
*   Algorithms:
    * Loop over files (for loop)
    * Error handling through usage()

### tail tool
Basically head function but upside down
Create a python function that accepts *command line args*, an optional modifier, a digit (n), and file name(s). Open file and read last `n` lines (n<=10 by defailt)

If multiple files, print `==> FILENAME <==` then the bottom `n` lines of the file (then repeat).

*   what I know:
    That my head function at least kina works
    * How to read a file in reverse

*   What I dont know:
    * Is the `reversed(list(file)` the best way to read the file backwards?
    * Other than that I think Im good? Wish me luck

*   Data needed:
    * commandline inputs, 
    * Files, modifier(flag)

*   Algorithms:
    * Loop over files (for loop)
    * Error handling through usage()

### cut tool
Create a function that takes *command line args*, and optional modifer (which requires an int after), and file name(s)
Open each file and print just the column (separated by `,`'s) that is requested
If multiple files, just do it in order without separation.

*   What I know:
    * How to split files with a separator
    * How to check for the modifier
    * There is a good chance i might need to fix an off-by-one error.
*   What I dont know:
    * what data type im going to get when I split the files.
*   Data needed:
    * command line inputs
        * optional modifier and integer for what row needs printin
        * files
*   Algorithms:
    * Loop over files (for loop)
    * Error handling through usage()

### paste tool

Create a function that joins 2 or more files together by combining files line by line, separated with a `,` .
If theres just one file, it acts like cat

*   What I know:
    * `",".join(array)` might do what i want
    * how to read the file
    * Im going to need to input each line into an array
*   What I dont know:
    * Why im not asleep

*   Algorithms:
    * Loop over files (for loop)
* Error handling through usage()

### tt.py 
Read what arguments have been given as an array.
there must be 2 or more args, the first will be the tool that is being used.
Pass all args after that into the tool wanted

*   What I know:
    * reading and poping from arrays

*   What I dont know:
    * how to read from command line
*   Data used:
    * list/array of args inputed from command line

*   Algorithms:
    * if this file, do this (for all files)
    * Error handling through usage()

## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.

### cat tool

cat(list_of_filenames):
"""
Take a list of filenames
for each file in the list of filename
open the file, print its contents to the screen with print()
"""
for filename in list_of_filenames:
    file = open(filename)  # Just let open() crash if filename is invalid
    for line in file:
        print the line, but suppress the extra newline afterward
    close file

### grep tool

grep(list_of_args):
"""
Take list of args
If first arg is `-v`: invert grep
else: next arg is the pattern to look for
for each file in filenames
open, search for pattern, print words with(-v: without) pattern.
"""
if list_of_args[0] = "-v":
    invert the grep function
    list_of_args.pop[0]
else:
    pattern = list_of_args[0]
    list_of_args.pop[0]
multFile = "" #empty string if theres only one file

for filename in list_of_args:
    file = open(filename)
    if list_of_args > 1:
        multFile = "{filename}:"
    for word in file:
        if word contains pattern && grep = true:
            print multFile + word (one per line)
        elif grep = false && word !contains pattern:
            print multFile + word (one per line)
    close file

### head tool
head(list_of_args):
    """
    Take a list of args
    check for modifiers to read length
    for each file in the list of filename
    open the file, 
    print the first n lines to the screen with print()
    """
    multFile = "" #empty string if only one file
    linesToRead = 10;
    if list_of_args[0] = '-v':
        linesToRead = int list_of_args[1]
        list_of_args.pop[0]
        list_of_args.pop[0] #left with only file names
    for filename in list_of_args:
        file = open(filename)  # Just let open() crash if filename is invalid
        if list_of_args > 1:
            multFile = "\n==> {filename} <=="
        count = 0
        for line in file:
            if count == linesToRead: break
            print the line, but suppress the extra newline afterward
            count += 1
        close file

### wc tool
wx(args):
    """
    Take a list of filenames
    for each file in the list:
    open the file, count lines, words, and characters
    print lines, words, characters, and filename
    """
    multFile = len(args) > 1 # true if more than 1 file
    total_line, total_word, total_char = 0
    for filename in args:
        file = open(filename)
        for line in file:
            if "" in line: # every char
                char_count +=1
            if " " in line: # check for words
                word_count +=1
            if "\n" in line: # check for lines
                line_count +=1
        print linecount, wordcount, charcount, and filename
        total_line += line_count
        total_word += word_count
        total_char += char_count
        file.close()

### sort tool
sort(args):
    """
    Take a list of filenames
    open all files, and sort each line by lexical order
    print all lines (from every file) in sorted order
    """
    for filename in args:
        file = open(filename)
        # store this somewhere or do something with it
        close file
    # take lines from every file and sort them
    print(sorted_lines)

### tac tool
tac(list_of_filenames):
    """
    Take a list of filenames
    for each file in the list of filename, starting at the bottom and going to the top
    open the file, print its contents to the screen with print()
    """
    for filename in list_of_filenames:
        file = open(filename)  # Just let open() crash if filename is invalid
        for the reverse of line in file:
            print the line, but suppress the extra newline afterward
        close file

### tail tool
tail(args):
    """
    Take a list of args
    check for modifiers to read length
    for each file in the list of filename
    open the file, reverse file
    print last (now technically first) n lines to the screen with print()
    """
    multFile = "" #empty string if only one file
    linesToRead = 10;
    if list_of_args[0] = '-v':
        linesToRead = int list_of_args[1]
        list_of_args.pop[0]
        list_of_args.pop[0] #left with only file names
    for filename in list_of_args:
        file = open(filename)  # Just let open() crash if filename is invalid
        if list_of_args > 1:
            multFile = "\n==> {filename} <=="
        count = 0
        for line in reversed file:
            if count == linesToRead: break
            print the line, but suppress the extra newline afterward
            count += 1
        close file

### cut tool
cut(args):
    """
    Take a list of args
    check for modifiers that will change what column is being printed
    for each file, print the specified column
    """
    if args has 0 arguments
        call usage
        quit
    column_to_cut = 1 # default
    # if there is a modifier and there is at least 3 args
    if first arg is `"-f"` 
        if len(args) >= 3 and second arg is an integer
            column_to_cut = args[1]
            pop the first 2 args (modifier and integer number)
        else: 
            incorrect input. call usage and exit
    # should be left with only file names as arguments now
    for file in args:
        open file
        split file into columns separated by `,`
        print the column specified by `column_to_cut - 1`
        
        
### paste tool

paste(args):
    If no args, just let open crash
    array_of_files = []
    for filename in args:
        open file
        for lines in file:
            if array index doesnt exist:
                append a new array index as ""
            add each line to the corresponding index in array_of_files
        close file
    print array_of_files as strings on separate lines
### tt.py

"""...The Code already Included..."""
else:
    tool = sys.args[0]
    sys.args.pop[0] #get rid of tool from array before passing into function
    if tool == "grep"
        grep(sys.args)
    if tool == "head"
        head(sys.args)
    # ...repeat for other tools...
    else:
        crash cause its not a tool 
        



## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.

### cat tool
*   As quoted in the provided Cat_Plan.md:
    - I forgot to account for all lines ending in `\n`, so I updated the plan to print without an added newline using the `end=""` parameter in python's `print()` function.
    * Turns out I forgot error handling through usage()

### grep tool

*   this went smoother than I thought and thats worrying
    * Turns out I forgot error handling through usage()

### head tool

*   The way I originally tried to account for multiple files resulted in `==> {filename} <==opponents`
    * I think I can fix that by printing it separatly right after I open the file
    * Turns out I forgot error handling through usage()

### wc tool

*   10/4 Code runs, but so far only the lines are counted correctly
    * I think my problem for words is that Im looking only for `" "`, but some(most) words in these files actually end in `"\n"`
*   10/5 Still don't know why the character count isnt working
    * Instead of using `if` for words, i used `len(line.split())`
    * Similarly, just `len(line)` gave me the correct character count.
    * Turns out I forgot error handling through usage()
    * 
### sort tool
  * Turns out I forgot error handling through usage()

### tac tool

*   When a `file` is read, its type is `<class '_io.TextIOWrapper'>` which cant be reversed().
    * calling reversed(list(file)) fixes that problem. 
        * How much memory does this take up?
        * This is simple, but is there a more memory efficient way?
  * Turns out I forgot error handling through usage()

### tail tool

*   10/5 My original plan of reversing the data and then reading it kinda works, but it prints it upside down
    * I either need to print them back in correct order, or find a different way to read the file.
*   10/6, through REPL testing, doing `for line in (file.readlines() [-linecount:])` might work. (can confirm)
    * Turns out I forgot error handling through usage()


### cut tool

*   having `column_to_cut` as an integer didnt account for multiple columns
    * Might be able to fix it by using `column_to_count` an array of ints
    * Turns out I forgot error handling through usage()
    * 
### paste tool

*   I kinda had to go relearn how to open and read files. I found that doing file.readlines() helped read the file in the way I wanted
*   Not going to lie, I forgot while loops existed. Might have been useful if i remembered that earlier.
    * Turns out I forgot error handling through usage()
* 
### tt.py

*   Way not as complicated as I thought. At least I assume that its working, I havent found a bug yet.

## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

**Most of my testing was done through the files in the provided testing folder.**

### cat
$ python src/tt.py cat data/ages8 data/dup5
Age
22
36
24
39
26
23
29
17
1
1
2
2
3
4
4
5

### tac
$ python src/tt.py tac data/ages8 data/dup5
17
29
23
26
39
24
36
22
Age
5
4
4
3
2
2
1
1


### head
$ python src/tt.py head data/ages8 data/dup5

==> data/ages8 <==
Age
22
36
24
39
26
23
29
17

==> data/dup5 <==
1
1
2
2
3
4
4
5

### tail
$ python src/tt.py tail data/ages8 data/dup5

==> data/ages8 <==
Age
22
36
24
39
26
23
29
17

==> data/dup5 <==
1
1
2
2
3
4
4
5

### grep
$ python src/tt.py grep 3 data/ages8 data/dup5
data/ages8:36
data/ages8:39
data/ages8:23
data/dup5:3

### wc
$ python src/tt.py wc data/ages8 data/dup5
9       9       28      data/ages8
8       8       16      data/dup5
17      17      44      total

### sort
$ python src/tt.py sort data/ages8 data/dup5
1
1
17
2
2
22
23
24
26
29
3
36
39
4
4
5
Age

### cut
$ python src/tt.py cut data/ages8 data/dup5
Age
22
36
24
39
26
23
29
17
1
1
2
2
3
4
4
5

### paste
$ python src/tt.py paste data/ages8 data/dup5
Age,1
22,1
36,2
24,2
39,3
26,4
23,4
29,5
17,

### tt.py

**This worked for all the other testing**


## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.

-   I needed to spend more time on cut and paste. I rushed those because I was running out of time, and that caused me to not quite understand all of it.
    - I was very much an "itchy reader" from the reading. I got the code I needed and left.
    - Because of this my documentation for these 2 programs are lacking and hard to understand.
    - However, because of how error handling was designed, bugs should still be easy to find the cause in a few months.
    - 
-   I feel like *most* of my documentation should make sense to others, but I understand even my rough english.
-   Unless anything drastic happens to python, this should stay viable code after upgrades.
    - I didnt import any extra libriaries other than what was needed. So as long as python stays reletivly similar, it should be fine.
    - 