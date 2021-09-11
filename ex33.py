# define function
def looper(start, stop):
    print "the beginning is %s: " % start
    print "the end is %s: " % stop

    i = start
    numbers = []

    while i < stop:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

#import modules
from sys import argv

script_name, input1, input2 = argv

in1 = int(argv[1])
in2 = int(argv[2])

looper(in1, in2)