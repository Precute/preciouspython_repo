mbox = open('mbox-short.txt')
# solution 1
for lines in mbox:
    line = lines.rstrip()
    if not line.startswith('From '):
        continue
    lins_in_list = lines.split()
    if len(lins_in_list) >= 2:
        print(lins_in_list[2])


# solution 2
# for line in mbox:
#     line = line.rstrip()
#     words = line.split()
#     if words is None or words == []:
#         continue
#     if len(words) < 1 words[0] != 'From':
#         continue
#     print(words[2])
