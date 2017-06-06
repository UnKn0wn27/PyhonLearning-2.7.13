from sys import argv

script, user_name, batman = argv
prompt = "> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
like = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
This is a line that has '%s' The Dark Knight in it.
Alright, so you sad %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (batman, like, lives, computer)
