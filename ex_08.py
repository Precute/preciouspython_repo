# parsing and extracting
str = 'X-DSPAM-Confidence: 0.8475'
st_position = str.find(' ')
print(st_position)
new_number = float(str[st_position+1 : ])
print(new_number)
