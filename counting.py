counts = dict()
# print("Enter a line of text")
# line = input('')
# words = line.split()
# print("Words:", words)
#
# print("Counting......")
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("Counts:", counts)

print("enter file name")
filename = open(input(''))
for line in filename:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print("The highest occurring word is", bigword, "and the number is", bigcount)
