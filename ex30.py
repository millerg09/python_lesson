people = 40
cars = 30
buses = 50

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "we can't decide"

if buses > cars:
    print "That's too many buses!"
elif buses < cars:
    print "maybe we could take the buses"
else:
    print "We still can't decide"

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."