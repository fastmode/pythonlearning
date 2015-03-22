#Program to open file, strip new lines, and turn all into upper case.
#Art Rodriguez  March 22, 2015
"""
Write a program that prompts for a file name, then opens that file and reads through the file, and print the 
contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt
"""

fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print "Invalid filename"
    exit ()

for line in fhand:
    line = line.rstrip().upper()
    print line
    
