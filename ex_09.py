# test file read
# first solution
# mbox = open('mbox-short.txt')
# lines = mbox.read()
# print(lines.upper())

# second solution
mbox = open('mbox-short.txt')
for lines in mbox:
    strip_line = lines.rstrip()
    print(strip_line.upper())
