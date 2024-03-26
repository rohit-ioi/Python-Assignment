# list = [40,20,30,10]
# newlist = []
# for i in list:
#     if i>25:
#         newlist.append(i)
# print(newlist)

list = [40, 30, 20, 10]
for i in list:
    newlist = [i for i in list if i>25]
print(newlist)   