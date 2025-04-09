#     *args - arguments,   **kwargs - keyword arguments

def my_func(*args):     # *args holds any number of arguments
  print(args)           # this prints the TUPLE args
  return  sum(args)    # sum - predefined function

print (my_func(1,2,3,4,5,6,7,8,9,10))


def my_func(*args, **kwargs):   # kwargs holds the values in a DICTIONARY
  total = 0
  for item in kwargs.values():
    total+= item                # adds the values in kwargs
  print(kwargs)                 # prints them
  return sum(args) + total      # returns the sum in args+ the sum in kwargs

print(my_func(1,2,3,4,5, num1 = 2, num2 = 10))


# General order if parameters when defining a function:                     (parameters, *args, default parameters, **kwargs)


# Functions Exercise:

def highest_even(li):
  highest = 0
  for item in li:
    if item % 2 == 0 and item > highest:
      highest = item
  return highest

print(highest_even([10,2,4,8,11])) #  Prints the highest even in the list

    # OR


def highest_even(li):
  nl = []
  for item in li:
    if item % 2 == 0:
      nl.append(item)
  return  max(nl)         # max returns the maximum number of a list