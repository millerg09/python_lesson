print "You enter a dark room with two doors. Do you go through door #1 or door #2"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear thinks you have a good singing voice and is intrigued by your vibrato"
        print "He drops the cake and walks toward you with a microphone. What do you do?"
        print "1. Sing loud and proud :D"
        print "2. Smile nervously and decline"
    else:
        print "I guess you can't follow instructions, eh?"

        sing = raw_input("> ")

        if sing == "1":
            print "You take the tenor and he sings a growly baritone. Live happily ever after."
        elif sing == "2":
            print "'You will regret this insult human' are the last words you hear."
        else:
            print "Well, doing %s saved you the public embarrassment!" % sing  
    #else:
        #print "Well, doing %s is probably better. Bear runs away." % bear


elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"