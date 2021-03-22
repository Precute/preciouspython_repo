datainput = open('romeo.txt')
letterdict = dict()
for line in datainput:
    line = line.rstrip()
    words = line.strip()
    for word in words:
        letterdict[word] = letterdict.get(word, 0) + 1
        # print(word)

letterlist = list()
for letter, counts in letterdict.items():
    newtuple = (counts, letter)
    letterlist.append(newtuple)
    print(newtuple)
#
# letterlist = sorted(letterlist)
# print(letterlist)
# letterlist = sorted(letterlist, reverse = True)
# print(letterlist)
