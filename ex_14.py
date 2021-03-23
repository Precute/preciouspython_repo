import re
openfile = open('mbox-short1.txt')
numlist = list()
for lines in openfile:
    lines = lines.rstrip()
    getlines = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', lines)
    if len(getlines) != 1 :
        continue
    print(getlines)
    num = float(getlines[0])
    numlist.append(num)
print("Maximum:",max(numlist))
