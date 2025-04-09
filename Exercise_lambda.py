my_list = [2,4,6]

# print a squared list based on my_list
print(list(map(lambda item: item**2, my_list)))



# List sorting
a = [(0,2), (4,3), (9,9), (10,-1)]  # a list of tuples that needs to be sorted

#def sor_key(item):
#  return item[1]

a.sort(key = lambda item: item[1])
print(a)


