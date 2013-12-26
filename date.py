print "Welcome to the online date picker! Let's start with your name. So, what is it?"
name = raw_input()
print "aah, so your name is %s. Mine too!! jk." % name
age = raw_input("How old are you? ")
if int(age) > 40:
    '''Note that raw_input is always going to result in a string so to turn a string of numbers into an integer object which can then have the greater than or less than sign applied to it, you must use int(string). To see what kind of object a variable is, you can use type(variable).'''
    print "You are too old to be dating. Get a life."
else:
    mf = raw_input("Great! so are you a male or female? [m/f] ")
    if mf == "f":
        print  "Sorry, this is a male-only dating service."
    else:
        print "Sorry, this is a female-only dating service."

