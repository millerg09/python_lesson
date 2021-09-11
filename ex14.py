from sys import argv

script, user_name, day_of_week = argv
hello = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to as you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(hello)

print "Where do yo live %s?" % user_name
lives = raw_input(hello)

print "What kind of computer do you have?"
computer = raw_input(hello)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Today is %s, did you know?
""" % (likes, lives, computer, day_of_week)