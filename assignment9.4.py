### Arturo Rodriguez
### April 20, 2015
### Python for Informatics
### Chapter 9 - Dictionaries
### Assignment 9.4
###
### Write a program to read through the mbox-short.txt and figure out who has the sent the 
###greatest number of mail messages. The program looks for 'From ' lines and takes the second 
###word of those lines as the person who sent the mail. The program creates a Python dictionary 
###that maps the sender's mail address to a count of the number of times they appear in the file. ###After the dictionary is produced, the program reads through the dictionary using a maximum loop 
###to find the most prolific committer.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"  #if Enter is pressed, the default file is provided
fhandle = open(name)

emails = dict()
address = list()

for line in fhandle:
    line = line.rstrip()                    #clears out all white space
    if not 'From ' in line : continue       #Skips any lines that don't contain this string
    words = line.split()                    #Puts all words in file into the line list
    address.append(words[1])                 #Appends only the email addresses to the address list
                 
for word in address:                  
    emails[word] = emails.get(word,0) + 1   #Adds email addresses from address list into emails dict

    print word, emails[word]                #Prints out appeareancesa and growing count
    
bigcount = None
bigemail = None
for email, count in emails.items() :            #Counts which email address appears the most
    if bigcount is None or count > bigcount :
        bigemail = email
        bigcount = count

print bigemail,"appears the most with ",bigcount," appereances."

#print emails.items()   
#print emails   
    
