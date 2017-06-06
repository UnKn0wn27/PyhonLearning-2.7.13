from sys import argv

script, a, b = argv

c = int(raw_input("Write a number : "))
d = int(raw_input("Write a number: "))

print """
a = %s
b = %s
c = %d
d = %d
c + d = %d
""" % (a, b, c, d, c + d)
