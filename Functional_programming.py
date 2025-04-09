# Functional programming is about:
      #- Clear and understandable
      # Easy to extend
      # Easy to mentain
      # Memmory efficient
      # DRY  

# It all reduces to PURE FUNCTIONS


                  # PURE FUNCTIONS

# Always return the same output, given the same input
# Doesn't produce any side-effects. (doesn't touch anything in the outside of the function)
# Example:

def multiply_by2(li):
  new_list = []                     # if we had this list declared outside the                                            function we would have produced side effects

  for item in li:
    new_list.append(item*2)
  
  return new_list                   # if we print here, it produces side_effects,                                          because the function will interact with the                                          outside world

print(multiply_by2([1,2,3])) 
print('')



                    # Map

# we can make the upper function like this:
# a map function, takes a function and an iterable and iterates trough it
# we can see it this way: map(action, what to act upon)
# It's a pure function; doesn't affect the outside world
# USED FOR ITERABLES

my_list = [1,2,3]

def multiply_by2(item):
  return item*2

print(list(map(multiply_by2, my_list)))  # In order to print a Map we need to convert                                             it to a list
print(my_list)
print('')



                  # FILTER

# can be used for filtering
# works on the same principle as the above


def odd_numbers(item):
  return item%2 != 0        # returns True or False

print(list(filter(odd_numbers, my_list)))




                    # ZIP

# used for zipping 2 iterables together
# they are zipped by indices (0 with 0, 1 with 1 etc.) into tuples


my_list = [1,2,3]
your_list = [6,4,8]

print(list(zip(my_list, your_list)))     # as many arguments as you want

print('')



                    # REDUCE

from functools import reduce        # that's how we import in Python


my_second_list = [1,5,7]

def ex_func(acc, item):
  print(acc, item)
  return acc+item

print(reduce(ex_func, my_second_list, 0))
print('')

# The reduce function takes as parameters: a function, an iterable, and a default value for acc.

# with every iteration the acc parameter gets modified with the previous returned Value

# the returned value of the reduce is the final returned value of ex_func

# reduce doesn't need list conversion





                      # Lambda expressions

# lambda param: action(param)

# they are functions which are used once
# so they don't take memory space
# they can be created on site


print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 == 0, my_list)))
print('')




                        # LIst comprehensions

my_list = [char for char in 'hello']   # basically, for each character in the iterable, append it to the list

print(my_list)


# we want to make a list with numbers from 0 to 100
my_list2 = [no for no in range(0,101)]

print(my_list2)
print('')


# we can have an expression inside the comprehension
# for example, we can multiply by 2 each number

my_list3 = [num**2 for num in range(0,101)]
print(my_list3)
print('')


# we can also put conditions

my_list4 = [num**2 for num in range(0,101) if num%2 == 0]

print(my_list4)
print('')




                      # Set comprehensions


# same as list comprehensions, but with the respective brackets


my_set = {num for num in range(0,100)}
print(my_set)
print('')



                      # Dictionary comprehensions

simple_dict = {
  'a' : 1,
  'b' : 2
}

my_dict = {key: value**2 for key,value in simple_dict.items() if value%2 == 0}

print(my_dict)

# we want to create a dictionary with key as the item in the list, and the value as the item  multiplied by 2

my_dict2 = {value: value*2 for value in [1,2,3]}
print(my_dict2)