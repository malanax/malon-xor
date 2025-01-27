# The first data structure we learned is Lists. We can find them in a previous repl.

# DICTIONARIES -> An unordered key-value pair

dictionary = {  #Syntax
    'a': 1,  # a -> key, 1 -> value.
    'b': 2
}

print(dictionary['b'])  #The value is accessed by the key. Prints 2
print('\n')

# A dictionary can contain various data types at once

dictionary = {
    'a': [1, 2, 3],  # -> even lists
    'b': 'Big',
    'c': True
}

#to access an indice of the list from the dictionary, the syntax is:

print(dictionary['a'][0], dictionary['a'][1], dictionary['a'][2])
print(dictionary['b'])
print(dictionary['c'])
print('\n')

#in the same way, a list can contain dictionaries

my_list = [{
    'a': [1, 2, 3],
    'b': 'Big',
    'c': True
}, {
    'a': [4, 5, 6],
    'b': 'Big',
    'c': True
}]

print(
    my_list[0]['a'][1]
)  # prints the first element from the list (a dictionary),the value of the key 'a' from the dictionary, the second item in that value(which is a list).

print(
    my_list[1]['a'][0]
)  # prints the second element from the list (a dictionary),the value of the key 'a' from the dictionary, the first item in that value(which is a list).
print('\n')

dictionary = {
    'masina': 'BMW',
    'salariu': '25 000$',
    'casa': 'penthouse',
    'copii': 3
}

print(dictionary)

print('Masina: ' + dictionary['masina'] + "\nSalariu: " +
      dictionary['salariu'] + '\nCasa: ' + dictionary['casa'] + '\nCopii: ' +
      str(dictionary['copii']))
print('\n')

# when it comes to when to use what, keep in mind that Lists are ordered and dictionaries aren't. So, a dictionary may be used in creating a user with different specificaions as example, where order of the info doesn't matter.

# A dictionary key needs to be imutable (a value that can not change).
# For example, we can use numbers or booleans as keys:

dictionary = {
    1: 'name',
    2: 'bichass',
    True: 'nigga',
    True: 'whiteboy'  # suprascrierea functioneaza in interiorul dictionarelor
}

print(dictionary[2], dictionary[True])
print('\n')

# But we can't use a list as a key:

''' dictionary = {     # block comment  ''' '''
  [100] : 2
}

print(dictionary[[100]])  '''   # this doesn't work because the values of a list can be changed; for example we can re-asign dictionry[0] with something else

# As a best practice,  a key is usually a descriptive STRING

#Dictionary Methods

#if we try to access something that dosn't exist in a dictionary, we will have an error that stops our program:

dictionary = {'age': 35, 'gender': 'Male'}

# print(dictionary['sex'])   -> this gives an error

print(dictionary.get('sex'))  # -> this does not

# GET() returns none if it doesn't find a value, and can also assign a value if it doesn't exist. If it exists, then the original value is returned. Ex:

print(dictionary.get('sex', 'Masculin'))
print('\n')

print(dictionary.keys())

########## Ex.
parv = 'gender'
for i in dictionary.keys():
  if parv == i:
    print('found it ' + dictionary.get(i))
###########
print('\n')

# Other way of creating dictionaries   -   NOT COMMON

#user = dict('name' = 'Mircea') # -> this doesn't work because the key must be a variable, not a datatype

user = dict(name='Mircea')  # -> this works
print(user)

# copy Method

user = {'gender': 'M', 'age': 26, 'color': 'whiteboy'}

# copy() - returns a copy of the dictionary.
# pop() - returns the value of the key and removes it

userbis = user.copy()
print(userbis)

userbis = user.copy().pop(
    'age'
)  # - > this stores the value of age, and removes it from the copy of user. SO, the user dict remains intact
print(userbis)
print(user)

print('\n')

# update() - updates the dictionary
#syntax: dictio.update({ x: y})

user.update({'hair coor': 'blue'})
print(user)

# we can test if something exists in the dictionary
print('age' in user)  # returns TRUE
print('characteristic' in user)  #returns FALSE
print('\n')

# we can search in keys or values
print('age' in user.keys())
print('age' in user.values())
print(user.items())  # items() returns every pair in the dictionary as a tuple

print(user.clear())  # clear() clears the dictionary, so this prints None.
print(
    user
)  # this way, it returns an empty dictionary. It was cleared at the previous line.

print('\n')

masini = {
    'Ferrari': 32000,
    'Lamborghini': 200000,
    'Dacia': 10000,
}

masini2 = masini.copy()  # Copied the list into masini2
masini.clear()  # Cleared masini
print(masini)
print(masini2)  # masini2 still contains the dictionary
print('\n')

# TUPLES

# Like lists but can't modify them - imutable, no sort, reverse, re-asignment
# Faster than lists
# If we don't need a list to change, use Tuple instead

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# my_tuple[0] = 2  # this gives an error due to imutability

print(my_tuple[2])  # we can access by index
print(5 in my_tuple)  # returns true

# we can use tuples as keys in dictionaries
user = {(1, 2): [1, 2, 3]}

print(user[(1, 2)])

# we can slice

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:2]  # starts at index 1 and ends before 2
print(new_tuple)  # a tuple of a single item. Has a comma at the and
print(my_tuple[1:3])
print('\n')

# we can assign the values from the tuples in variables

x = my_tuple[0]
y = my_tuple[1]
print(x + y)

#OR with Unpacking

x, y, *rest = my_tuple  # x, y are the first 2 values, and the rest are stored in the                            list "rest"
print(x, y, rest)
print(type(rest))
print('\n')

# Tuple methods

# count()  - counts how many times an item is present
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(5))

#index() - returns the index of a value
print(my_tuple.index(5))

#length
print(len(my_tuple))
print('\n')

# SETS

# Unordered collections of unique objects

my_set = {1, 2, 3, 4, 5,
          5}  # the values are not stored one next to the other - Unordered
print(
    my_set
)  # it only returns the unique items. Can't have duplicates, so                                the second 5 is never added
print(len(my_set))

my_set.add(100)
my_set.add(2)  # this isn't added because it already exists in the set
print(my_set)
print('\n')

# Exercise:

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  #  Converting a list to a set
##########

my_set = {1, 2, 3, 4, 5}
#print(my_set[0])      # error -> cannot access by index. The alternative is:
print(2 in my_set)

new_set = my_set.copy()  # copy() copies the set
my_set.clear()  # clear() clears the set
print(new_set)  # this contains the copy
print(my_set)  # the original set is cleared
print('\n')

# Set Methods

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# Difference
print('Difference')
print(my_set.difference(
    your_set))  # returns the items that are not found in the second set
print('\n')

#Discard
print('Discard')
your_set.discard(10)  # the element gets discarded
print(your_set)
your_set.add(100)  # adds the element
print(your_set)

print(
    your_set.discard(5)
)  # this returns none, but the action is valid though the                                      function is applied into a print function (general rule)
print(your_set)  # we can see here
your_set.add(5)
print('\n')

# Difference_update
print('Diffference update')
print(my_set.difference_update(your_set))
print(my_set)  # the set is updated, now containing only the difference

my_set.add(4)  # we add back the difference.
my_set.add(5)  # the add method suports only 1 argmunet
print('\n')

# Intersection
print('Intersection')
print(
    my_set.intersection(your_set))  # prints the common elements in the 2 sets
print(my_set & your_set)  # Same thing/ shortcut
print('\n')

# Isdisjoint
print('Isdisjoint')
print(
    my_set.isdisjoint(your_set)
)  # returns FALSE if they have common elements, TRUE  if they are different
print('\n')

# Union
print('Union')
print(my_set.union(
    your_set))  # Unites the sets toghether. Of course, no duplicates
print(my_set | your_set)  # Same thing/ shortcut
print('\n')

# Issubset
print('Issubset')

my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.issubset(
    your_set))  # returns TRUE if the 1st set is a subset of the 2nd
print('\n')

# Issuperset
print('Issuperset')

print(
    my_set.issuperset(your_set)
)  # returns FALSE if the 1st set is not a superset of                                          the 2nd
print(your_set.issuperset(
    my_set))  # returns TRUE if the 1st set is a superset of the 2nd
