# imports the `argv` module from sys
from sys import argv

# sets up the script name and input_file as script argument variables
script, input_file = argv

# creates the first function `print_all`, which accepts one input variable `f`
def print_all(f):
    # the function is designed to use the read function with no extra parameters
    print f.read()

# creates the second function "rewind", which accepts one input variable `f`
def rewind(f):
    # the function goes back to the first byte of the input file `f`
    f.seek(0)

# creates the third function "print a line", which accepts two input variables
def print_a_line(line_count, f):
    # this function prints `line_count` and a readline function from `f`
    print line_count, f.readline()

# opens the input file from the script argument and assigns opened file to a variable
current_file = open(input_file)

# prints a string decribing what we are about to do
print "First let's print the whole file:\n"

# uses the function `print_all` and passes one input variable in `current file`
# print all will go ahead and print out the "read" input->current file
print_all(current_file)

# prints a string describing what we are about to do
print "Now let's rewind, kind of like a tape."

# calls the `rewind` function and passes in one input variable
rewind(current_file)

# prints a string describing what we are about to do
print "Let's print three lines:"

# creates a variable and assigns an integer value of 1
current_line = 1
# calls the `print a line` function with two input variables: 1, "input file"
print_a_line(current_line, current_file)

# recursively increments 1 to the current_line variable and the prints the line
current_line = current_line + 1
print_a_line(current_line, current_file)

# recursively increments 1 to the current_line variable and the prints the line
current_line = current_line + 1
print_a_line(current_line, current_file)