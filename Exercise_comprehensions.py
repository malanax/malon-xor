some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#duplicates = []
#for value in some_list:
#    if some_list.count(value) > 1:
 #       if value not in duplicates:
 #           duplicates.append(value)

duplicates = [item for item in some_list if some_list.count(item) > 1]

print(list(set(duplicates)))


#    OR

#duplicates1 = list(set([item for item in some_list if some_list.count(item) > 1]))

#print(duplicates1)



some_list2 = ['a','b','c', 'd', 'b', 'e', 'e', 'e']

doubles = [item for item in some_list2 if some_list2.count(item)>1]
print(set(doubles))