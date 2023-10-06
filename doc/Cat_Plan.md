# Software Development Plan

## Phase 0: Requirements Specification

Design a tool that prints the contents of a list of files

This program will use the arguments given by the user running it through `sys.argv`. The expected input will be a list of file paths. If any invalid paths are given, the program will crash with a `FileNotFoundError` when that path is reached. Otherwise, each line of each file will be printed. 

The `cat` function will make use of a for loop that iterates though each file path in the given arguments, and a nested for loop that iterates through each line in each file. 

The driver code in `tt.py` will call the `usage` function if there are no arguments given or no valid tool was given. If the given tool is `"cat"`, it will call on the `cat` funtion, passing in all remaining arguments. 

## Phase 1: Design

- Driver code in `tt.py`:
    - if the length of arguments is 1, no arguments were given by the user:
        - call `usage` with an appropriate error message.
    - check the second argument (`sys.argv[1]`):
        - if it is `"cat"`:
            - if the length of `sys.argv` is exactly 2, call `usage` with an appropriate error message, passing `"cat"` in as the `tool` argument.
            - else call `cat`, passing in the remaining arguments.
        - if it is not a valid tool:
            call `usage` with an appropriate error message.

- Function `cat` takes a list of strings as its parameters
    - for each string in args:
        - attempt to open the string as a file path (will raise a `FileNotFoundError` if given an invalid path).
        - for each line in the opened file:
            - print the line without an added newline (use `end=""`).
        - close the file.

When passed a list of valid file paths (such as `[data/words5, data/let3, data/names10]`), the contents of each file will be printed in that order. When given no valid file paths (such as `[data/DOES_NOT_EXIST]`), the program should crash with a `FileNotFoundError`. When given a mix of valid and invalid arguments (such as `[data/words5, data/let3, data/DOES_NOT_EXIST, data/names10]`), the contents of each valid file until the invalid one should be printed like normal, and then the program should crash with a `FileNotFoundError` and give no further output, even though the remaining files might be valid. 


## Phase 2: Implementation

- I forgot to account for all lines ending in `\n`, so I updated the plan to print without an added newline using the `end=""` parameter in python's `print()` function.


## Phase 3: Testing and Debugging

### Test 1 - One valid argument
1. In the command line, enter `python3 src/tt.py cat data/ages8`
2. Verify that the output matches the contents of `data/ages8`

#### Result: Passed

### Test 2 - Multiple valid arguments
1. In the command line, enter `python3 src/tt.py cat data/words5 data/let3 data/names10`
2. Verify that the output displays the contents of `data/words5`, `data/let3`, and `data/names10` in order without crashing

#### Result: Passed

### Test 3 - One invalid argument
1. In the command line, enter `python3 src/tt.py cat data/DOES_NOT_EXIST`
2. Verify that the program crashes with a `FileNotFoundError` and gives no additional output

#### Result: Passed

### Test 4 - Mixture of valid and invalid arguments
1. In the command line, enter `python3 src/tt.py cat data/words5 data/let3 data/DOES_NOT_EXIST data/names10`
2. Verify that the contents of `data/words5` and `data/let3` are printed in order
3. Verify that the program crashes with a `FileNotFoundError`
4. Verify that nothing is printed after crashing

#### Result: Passed

### Test 5 - No arguments
1. In the command line, enter `python3 src/tt.py cat`
2. Verify that the code exits with a `usage` message for the `cat` tool (and no other tools are present in the `usage` message)

#### Result: Passed

### Test 6 - No tool
1. In the command line, enter `python3 src/tt.py`
2. Verify that the code exits with a `usage` message describing every tool.

#### Result: Passed

### Test 6 - Invalid tool
1. In the command line, enter `python3 src/tt.py invalid`
2. Verify that the code exits with a `usage` message describing every tool.

#### Result: Passed

## Phase 4: Deployment

- I verified that my most recent commit with my complete implementation and testing phases was pushed to GitLab
- I verified that the project's url was correct
- `Concatenate.py`, `Partial.py`, `WordCount.py`, `Grep.py`, `CutPaste.py`, `Sorting.py`, and `tt.py` are all present in the remote repository's `src` directory
- I cloned my repository in another location on my computer and ran all the tests again, and it still passed all test cases
- I verified that `doc/Plan.md` and `doc/Signature.md` were both still present in the remote repository


## Phase 5: Maintenance

- This program should be very straightforward and simple to understand
- Because the code is short and the documentation is robust, I should be able to pinpoint the cause of any bugs fairly quickly.
- The documentation is written very descriptively, so anybody else should be able to understand it, including myself in the future. 
- New features should be easy to add. New text tools will just take another case in `tt.py` and a new function to implement them.
- Because this program is run through the shell using only built-in Python functions, it should theoretically run through the shell of any computer that has the Python interpreter installed. 
- As long as the latest version of Python keeps the functionality of its basic built-in functions intact, this program should run on any future version of Python. 
