                    # Higher order function - HOC

# A function which accepts another function as a parameter
# OR a function which returns another function

def greet(func):
  func()

def hello():
  print('Helloo')

print(greet(hello))


###

def greet2():
  def hi():
    print('Hi')
  
  return hi()

print(greet2())
print('')



# Decorator

def my_decorator(func):   # takes the function declared inside as parameter
  def wrap_func():        # decorates the function defined in the decorator
    print('********')
    func()
    print('********')
  return wrap_func

@my_decorator       # inside this decorator, everithing that's declared happens. It                          can have only 1 function inside
def hello():
  print('Hello')

@my_decorator
def bye():
  print('See ya!')

hello()
bye()
print('')

# How decorators work. The above is the same as

#hello2 = my_decorator(hello)
#hello2()

# OR

my_decorator(hello)()
print('')


# What happens if we declare the function inside the decorator with a parameter


#@my_decorator
#def hello3(greeting):
#  print(greeting)

#hello3('HI')        # Error because the function in the argument doesn't take arguments


  # we can do it like this:

def my_decorator2(func):
  def wrapper(greet):
    print('*****')
    func(greet)
    print('*****')
  return wrapper

@my_decorator2
def hello4(greeting):
  print(greeting)

hello4('Hello')
print('')


# Decorator Pattern
# this pattern is used all over the places
# it gives flexibility and functionality

def my_decorator3(func):
  def wrapper_function(*args, **kwargs):
    func(*args, **kwargs)
  return wrapper_function

@my_decorator3
def greeting(message):        # we can give a single argument
  print(message)
greeting('Hi')

@my_decorator3
def greeting1(message, smilyface=':)'):        # we can give a single argument, and a                                                  keyword argument, or as many as we want
  print(message, smilyface)

greeting1("Hi")





# We can do a Performance decorator to illustrate better how it works
# We will do a functions which executes a long calculation and calculate how much time it takes.
from time import time

def performance(func):
  def wrapper(*args,**kwargs):

    t1 = time()
    result = func(*args,**kwargs)
    t2 = time()
    print(f'It took {t2-t1} s')
    return result
    
  return wrapper

@performance
def calculate():
  for i in range(100000000):
    i*5

calculate()




    
