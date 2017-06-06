#raw_input() presents a prompt to the user(the optional arg of raw_intput([arg])
#gets input from the user and returns the data input by the user in a string.
#Exemple:
# name = raw_input("What is your name?")
# print "Hello, %s." % name 
#raw_input was renamed input() in Python 3
print "How old are you?",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(
    age, height, weight)
