"""
def while_function():
    i = 0
    n = 9
    numbers = []

    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        m = int(raw_input("Nr > "))
        i += m
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

while_function()
"""

def for_function():
    numbers = []

    for i in range(1,6):
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the buttom i is %d" % i

for_function()
