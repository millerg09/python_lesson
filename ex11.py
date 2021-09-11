print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "What is your name?",
name = raw_input()

print age, height, weight, name

print "So, you're %s years old, %s tall and %s heavy and your name is %s." % (
    age, height, weight, name)

math = int(age) * int(weight)
print "Your age times your weight is: ", math