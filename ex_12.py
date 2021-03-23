word_dict = dict()
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
        word_dict[word] = word_dict.get(word, 0) + 1
# print(word_dict)
maxlength = 5
newdic = list()
for word, counts in word_dict.items():
    newtuple = (counts, word)
    newdic.append((newtuple))
# print(newdic)
newdic = sorted(newdic, reverse = True)
# print(newdic[:maxlength])
for v,k in newdic[:maxlength]:
    print(v,k)
