"""
March 22, 2015  Art Rodriguez
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
 X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of 
those values and produce an output as shown below. You can download the sample data at 
http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

""" Example to slice data and turn into float
text = "X-DSPAM-Confidence:    0.8475";
numpos = text.find("0")
number = text[numpos: ]
print float(number)
"""

fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print "Invalid filename"
    exit ()

count = 0
appearances = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    numpos = line.find("0")
    number = float(line[numpos: ])
    appearances = appearances + number
    #line = line.rstrip()
    #print line
#print count
average = appearances / count
print "Average spam confidence:", average
    
