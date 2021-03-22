d = {'a':10, 'c':22, 'b':1}
# # exercise 1
# d.items()
# print(d.items())
# sorteddic = sorted(d.items())
# for key, value in sorteddic:
#     print(key, value)

# execise 2
temp_list = list()
for key, value in d.items():
    temp_list.append((value, key))
print(temp_list)
temp_list = sorted(temp_list)
print(temp_list)
temp_list = sorted(temp_list, reverse=True)
print(temp_list)
