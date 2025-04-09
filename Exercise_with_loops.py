picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


#while n <= len(picture)-1:
 # for i in picture[n]:
  #  if picture[n][i] == 0:
   #   picture[n][i] = my_dict[picture[n][i]]
    #elif picture[n][i] == 1:
     # picture[n][i] = my_dict[picture[n][i]]   

#  n = n + 1

#print(picture, end = ' ')


#n = 0
#while n <= len(picture)-1:
 # for i in picture[n]:
  #  if picture[n][i] == 0:
   #   print('', end = '')
    #else:
     # print('*', end = '')
  #print('\n')
  #n+=1

for row in picture:                       # in this case the better choice is FOR
  for pixel in row:
    if pixel == 0:
      print(' ', end = '')      # print ends by default with '\n', so we change that                               with '' so we can print on the same row
    else:
      print('*', end = '')
  print('')                      # print ends by default with '\n' so we new line here


# since 1 is true, we can clean the code:

for row in picture:                       # sane thing but cleaner code
  for pixel in row:
    if pixel:
      print('*', end = '')
    else:
      print(' ', end = '')
  print("")


# Ex 2: Print the duplicate values

listn = ['a','b','c','b','d','m','n','n']
count = 0
my_list = []

for item in listn:
  if listn.count(item) > 1:
    my_list.append(item)
    listn.remove(item)

# or

for item in listn:
  if listn.count(item) > 1:
    if item not in my_list:
      my_list.append(item)
  
  

print(my_list)
  