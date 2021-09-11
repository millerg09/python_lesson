from sys import argv

script, filename = argv

print "Okay, we're going to begin by confirming we are opening the right file: %s" % filename
target = filename

txt = open(target)

print "Here's your file: %s" % filename

print txt.read()