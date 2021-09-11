# here you set up a bunch of variables, some with strings inside of the strings using formatters
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not) # string insertion

# here we print some simple variables
print x
print y

# here we print some variables that have other variables inside them, as strings
print "I said: %r" % x # string insertion
print "I also said: '%s'." % y # string insertion

# this is setting up the joke evaluation with a boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# this concats the two variables together
print joke_evaluation % hilarious

# this sets up some simple variables
w = "This is the left side of..."
e = "a string with a right side."

# and then prints them using string addition
print w + e