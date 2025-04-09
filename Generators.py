# Generators allow us to generate a sequence of values over time

# Example of generator:
#print(list(range(1000000)))   # This generates a number at a time up until 100000000

# When creating a list of a range, it takes a lot of computers memmory.

# A generator is an iterable
# Not every iterable is a generator
# The difference between the 2 is how we implement them

def generator_function(num):
  for i in range(num):
    yield i * 2           # yield is a keyword that pauses the function for each value                         of i, then act upon it. Yield also turns the function into                         a generator

g = generator_function(100)
print(g)                  # this prints that g is a generator
next(g)                   # here we have the value 0
next(g)                   # here we have the value 1
print(next(g))            # here we have the value 2, so it prints 4



# After 'next()' is called, the generator remembers the last value and comes back to where it's left
# If we call next() more times than values in the generator, we get a StopIteration error


# Generators are useful when calculation large sets of data. - RESOLVER.
# Here is an example:

from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(10000000):               # Generator   -  Faster
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):         # List    - This doesn't finish
        i*5


long_time()
#long_time2()




#############


# We can create our own generator:

class My_Gen():

  current = 0

  def __init__(self, first, last):          # Constructor
    self.first = first
    self.last = last
  
  def __iter__(self):                       # We make the object an interable
    return self
  
  def __next__(self):
    if My_Gen.current < self.last:      # if current value < than the last value
      num = My_Gen.current              # store the value
      My_Gen.current += 1               # increment the current value
      return num                        # return the stored value
    raise StopIteration

gen = My_Gen(0, 100)
for i in gen:               # The for loop stops iterating when it encounters the err
  print(i)

  
