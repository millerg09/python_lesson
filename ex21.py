def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def div(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do same math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = div(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ %d" % (age, height, weight, iq)

# a puzzle for the extra credit, type it in anyway.
print "here is a puzzle."

what = add(age, subtract(height, multiply(weight, div(iq, 2))))

a = div(iq, 2)
b = multiply(weight, a)
c = subtract(height, b)
d = add(age, c)

print a, b, c, d

print "that becomes: ", what, "can you do it by hand?"