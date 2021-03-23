import re
openfile = open('mbox-short1.txt')
for line in openfile:
    line = line.rstrip()
    if re.search('From:', line): #regular expression 
    # if line.find('From:') >= 0:
        print(line)
