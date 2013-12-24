print "Welcome to the online date picker! Let's start with your name. So, what is it?"
name = raw_input()
print "aah, so your name is %s. Mine too!! jk." % (name)
age = raw_input("How old are you? ")
if age > 40:
    print "You are too old to be dating. Get a life."
else:
    print "Great! so are you a male or female? just type m or f."
    if raw.input() == "f":
        print  "Sorry, this is a male-only dating service."
    else:
        print "Sorry, this is a female-only dating service."
    
