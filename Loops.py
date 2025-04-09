                            #  FOR loops

# SYNTAX: for item(i,n,'name') in x(any data_type) : 
#             instructions..
# for each item(-> a variable we declare to pass through every element in the one we want, for example <-'x') do the instructions below

for i in 'Zero to mastery':    # 'Zero to mastery is called an iterable'
  print(i)
print('\n')

for i in [1,2,3,4,5]:          # [1,2,3,4,5] is called an iterable. Something you can                                   iterate through
  print (i)
print('\n')

for i in {1,2,3,4,5}:           # Set
  print(i)
print('\n')

for i in (1,2,3,4,5):           # Tuple
  print(i)
print('\n')

#for i in 10:                  # Error because int isn't iterable
#  print(i)

# Example of capitalizing letters
text = 'Zero to mastery'
textU = ''
for item in text:
  textU = textU + item.upper()

print(textU)
print('\n')

# Example and ilustration of nesting fors

listx = [1,2,3,4,5]
for item in listx:
  for i in ['a','b','c']:
    print (item, i)

print(item)   # After the cycle ends, the iterators equal the last value: 5
print(i)      # And i equals c
print('\n')


# Example with dictionaries

users = {
  'name' : "Boogie Man",
  'age' : 25,
  'young' : True
}

for item in users:              # item iterates through the KEYS
  print(item, users[item])      # Here we print the key and the correspondent value
print('\n')

for item in users.items():      # iterate through the items. Tuples of keys and values
  print(item)
print('\n')

for item in users.values():     # iterate through the values
  print(item)
print('\n')

for item in users.keys():       # iterate through the keys
  print(item)
print('\n')

for key, value in users.items():    # we can use multiple variables to iterate
  print (key, value)
print('\n')



# Exercise

my_list = [1,2,3,4,5,6,7,8,9,10] 
sum = 0

for i in my_list:
  sum = sum + i
print (sum)
print('\n')



# RANGE() - ranges between 0 and a number-1, or in a certain range

print(range(100))    # ranges between 0 and 100
print(range(0, 100)) # same

for item in range(0, 100):    # iterates 100 times
  print(item)
print('\n')

  # we can use _ as a name for the iterator
for _ in range(0, 10):
  print(_)
print('\n')

  # range() has a 3rd parameter which skips items by a number
for _ in range(0, 10, 2):   # this prints from 2 to 2
  print(_)
print('\n')

  # if we want to iterate in reverse, we use -1 as the 3rd parameter
for _ in range (10, 0, -1):    # without -1 it doesn't work
  print(_)
print('\n')

  # we can easily create lists using range()  :  list( range(n) )
for _ in range(2):
  print(list(range(0, 10)))
print('\n')


my_list = []
for _ in list(range(0,9)):
  my_list.append(_)
print(my_list)

my_list = list(range(0,9))
print(my_list)


# if extended - reminder
no = 4.5

print(4.6) if no == 4.6 else print('Something else')

if no == 4.5:
  no = 5
else:
  no  = 10
print (no)
print('\n')



# ENUMERATE() - enumerates an iterable by index and character
      # Useful if you need the index counter of the item you're looping through

for i in enumerate('Hello'):   
  print(i)                      # this form prints tuples with index and character
print('\n')

for i, char in enumerate('Hello'):    # using unpacking, we print index and char on 2                                          separate columns
  print(i, char)
print('\n')

for i, char in enumerate([1,2,3]):
  print(i, char)


  # exercise: Find the index of the item with value 50 in a range of 100
container = 0;
for i, char in enumerate(list(range(100))):
  if char == 50:
    container = i
print(container) 

  # simpler: 
for i, char in enumerate(list(range(100))):
    if char == 50:
      print(f'The index of 50 is: {i}')    # this is using text formating. we save                                            memory by not creating another variable

print('\n')

                          #  WHILE LOOP


# Syntax: while condition:
          #  instructions
# also suports else:

n = 0

#while n < 10:                 # this gives an infinite loop, because n is always 0
#  print(n)


while n < 10:                  # prints  numbers 0 - 9
  print(n)
  n = n+ 1                     # n = 0+1,2+1,3+1 etc. Keeps the value outside the loop
else:
  print("Number isn't 0-9")           # when reaching 10, we go in the else: statement
print('\n')

# break - breaks the loop, jumps over 'else:' also
n = 0
while n < 10:                 # while n is less than 10
  print(n)                    # print n
  n = n+ 1                    # raise n by 1
  break                       # In this case we break after the first value is printed
                              # and if we print n outside the loop we should have 1
else:                         # else is executed only if there isn't a break statement
  print("Number isn't 0-9")   # if the number isn't less than 10, print this

print(n)
print('\n')


#   FOR vs WHILE
# For are great for simple loops
# While are great for complex loops and conditions. For example we can do:

while True:                       # while True (always)
  response = input('Say smth: ')  # response = input we make
  if response == 'bye':           # if the input is 'bye'
    print('Byebye')               # then print 'byebye'
    break                         # and break the while loop

# BREAK can be used in a for also:
my_list = [1,2,3]
print(len(my_list))
for i in my_list:
  print(i)
  break               # it breaks after the 1st element gets printed
print('\n')


# CONTINUE - the loop goes to the first line on the next iteration. Everything below                continue doesn't execute

for i in my_list:
  print(i)                # this prints normal
  continue                # this is continued to the first line
  print(i)                # so this doesn't execute
print('\n')

n = 0
while n < len(my_list):
  n += 1 
  continue                 # IDEM   
  print(my_list[n])
  n += 1                    
print('\n')

# PASS - is a pleaceholder. ex:

for i in my_list:             # if a loop is left empty, it generates an error
  pass                        # so we use pass to placehold and avoid that.
  