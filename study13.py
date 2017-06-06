print "Calculate 2 numbers."

nr1 = int(raw_input("Nr1: "))
nr2 = int(raw_input("Nr2: "))

print "Choose what equation you want to make."
print "1. +"
print "2. -"
print "3. *"
print "4. /"

nr = int(raw_input("Choose option: "))

if nr == 1:
    print "Answear: %d" % (nr1 + nr2)
elif nr == 2:
    print "Answear: %d" % (nr1 - nr2)
elif nr == 3:
    print "Answear: %d" % (nr1 * nr2)
elif nr == 4:
    print "Answear: %d" % (nr1 / nr2)
else:
    print "There is no such optionself."
