#inputs variable from script(or system i think) into argv
from sys import argv
#give variables arguments from argv(which is a module)
script, filename = argv
#open the file.txt
#or txt = open('filename') or txt = open.("filename")
txt = open(filename)
#write file.txt name
print "Here's your file %r:" % filename
#write everything in terminal thats writen in the file.txt
print txt.read()
#closing file txt
txt.close()
#rewrite the txt file name again
print "Type the filename again:"
file_again = raw_input("> ")
#open it
txt_again = open(file_again)
#read id
print txt_again.read()
txt_again.close()
