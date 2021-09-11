# attempt at your own function
def avg(arg1, arg2, arg3):
    print "Now it's time for some math\n"
    print "Let's calculate the average of three numbers"
    total = int(arg1) + int(arg2) + int(arg3)
    avg = total / 3.0
    print avg

print "We can just insert values like '1, 4, and 10'"
avg(1, 4, 10)

print "And we can assign variables using arguments."

arg1 = raw_input("Your first number: ")
arg2 = raw_input("Your second number: ")
arg3 = raw_input("Your second number: ")

avg(arg1, arg2, arg3)
