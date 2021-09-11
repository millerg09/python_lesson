# create a list with brackets, and assign the list to a variable
the_count = [1, 2, 3, 4, 5]
# another list to a variable
fruits = ['apples', 'oranges', 'pears', 'apricots']
# another list to a variable, with both integers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

"""
# this first kind of for-loop goes through a list
for a_new_variable in the_count:
    print "This is count %d" % a_new_variable

# same as above
for fruit in fruits:.py

    print "A fruit of type: %s" % fruit

# also we can go through mixes lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)


# now we can print them out too
for i in elements:
    print "Element was: %d" % i

"""
"""
students = ["Anna", "Bob", "Charlie", "Diana", "Eric", "Fannie"]

for sub_name in students:
    print "The student's name is %s" % sub_name

print "\n next section \n"

print "the first student's name is", students[0]

"""
weather = [["M", "T", "W", "Th", "F", "Sa", "Su"],["Sunny", "Rainy", "Cloudy", "Windy", "Drizzle", "Snow", "Frost"]]

print (weather[1][2])

for forecast in weather[1]:
    print "This day will be: %s" % forecast
