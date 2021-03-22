counts = dict()
print("enter file name")
filename = input('')
if len(filename) < 1:
    filename = 'clown.txt'
filename = open(filename)
for line in filename:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # print(word)
        counts[word] = counts.get(word, 0) + 1
maxcount = None
commonword = None
for word,count in counts.items():
    print(word, count)
    if maxcount is None or count > maxcount:
        commonword = word
        maxcount = count
print("The highest occurring word is", commonword, "and the number is", maxcount)
