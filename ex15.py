# import a python module for use in your script
from sys import argv

# assign variables to the input arguments
#script, filename = argv

filename = raw_input("What file do you want to open?: \n>")

# use the open function on the variable `filename`
# and assign the opened output to a new variable
txt = open(filename)

# print the variable from filename
print "Here's your file %r: " % filename
# print the output of the opened file
print txt.read()

# promt to type the filename again
print "Type the filename again: "
# user input of a filename, assigned to new variable
file_again = raw_input("> ")

# `open` function to open the file, assigned to new variable
txt_again = open(file_again)

# print the read output of the opened file
print txt_again.read()