print "Let's practice everything."
print 'You\'d nee to know \'bout escapes with \\ that do \n and \t tabs'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and required an explanation
\n\twhere the is none.
"""

print "----------------------------------"
print poem
print "----------------------------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
#def can return multiple variables WOW TEHNOLOGY!
def secret_formulat(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formulat(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point /= 10

print "We can also say like this:"
print "We'd have %d beans, %d jars, and %d crates" % secret_formulat(start_point)
