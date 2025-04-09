                            # Functions
                        
def hello():                # key word 'DEF' - name() - column :
  print('Hello!')           # instructions

hello()                     # call the function
print('\n')

# Functions help us keep the code DRY, and re-use easily a block of chr

tree = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [0,0,0,1,0,0,0]
]

def show():
  for row in tree:
    for index in row:
      if index == 0:
        print(' ', end = '')
      else:
        print('*', end = '')
    print("")
show()
print('\n')


# Parameters are the variables we give a function
# Parameters are used when we define the function

def message(name, emoji):               # name and emoji are arguments
  print(f'Hello {name}{emoji}')


# Arguments are used when we provide actual values to a function
# Arguments are used when we call the function

message('Alex', ':D')                   # Alex and :D are arguments
message('Vlad', ':D')
message('Robert', ':D')


def greet_babe(greet, apelative):
  print(greet+' '+apelative+'!')

greet_babe("Sap",'babe')
print('')


def celsius_to_fahr():
  celsius = int(input("Introduceti temperatura: "))
  f = (celsius*1.8)+32
  print(f"Temperatura in grade Fahrenheit este {f}")

celsius_to_fahr()
print('')





def message(name, emoji):               # name and emoji are POSITIONAL arguments
  print(f'Hello {name}{emoji}')

message('Alex', ':D')             # the arguments must be provided in the parameters                                       order, so POSITION matters
message(':D', 'Alex')    
    
    # but we can use KEYWORD arguments where order doesn't matter (BAD PRACTICE):

message(emoji=':)', name='Alex')



    # Default Parameters

def message(name='Darh Vader', emoji = ':x'):
  print(f"Hello {name}{emoji}")

message()               # This uses the default Arguments
message("alex",':P')    # This overwrites the default and uses the given arguments 
message("Alex")         # This overwrites only the name parameter
message(emoji=":(")     # This overwrites only the emoji parameter




#    RETURN

def sum(num1,num2):
  num1 + num2

print(sum(4,5))          # this doesn't do anything, because the function doesn't                                 return anything

def sum(num1,num2):
  return num1 + num2
print(sum(3,4))           # This does. Return returns the value so it can be used

# As general rules, a function must:
  # Do one thing really well
  # Return something, or pirnt something.

def sum(num1,num2):
  return num1 + num2

total = sum(5,10)       # The returned value is stored in total
print(sum(10,total))    # This sums 10 and the value in total
print(sum(10,sum(5,10)))  # IDEM

        # Return automatically exists the function

#  We can NEST

def sum(num1,num2):           # Defines sum with num1,num2 parameters
  def inside_func(n1,n2):     # Defines insed_func inside the sum function
    return n1+n2                  # which returns n1+n2 
  return inside_func(num1,num2) # The sum function returns what inside_function                                        returns with the sum parameters by calling inside_fun
print(sum(2,3))           # call the sum function




# Methods are functions belonging to a datatype.

'Hello'.capitalize()   # capitalize() belongs to string




#  Docstrings -> an explanation of he function

def functios(p):
  '''
  This function prints parameter p      # this is a docstring
  '''
  print(p)

functios("HEY")         # if we hover over the function we see the indication in                                 docstring
help(functios)          # help returns the docstrings in functions.
print(functios.__doc__) # IDEM
print('')


          #   CLEANUP CODE

def is_even(number):
  if number % 2 == 0 :
    return True
  elif number % 2 != 0 :      # This is accomplished only with else, so it's not needed
    return False

print(is_even(51))


def is_even(number):
  if number % 2 == 0 :
    return True             # As return exits the if automatically if the no is even, and by that                              returning of False would not be reached if the no is even, we can                                remove else, because return False would be reached only if the number                            is not even
  else:                   
    return False
print(is_even(51))


def is_even(number):         
  if number % 2 == 0 :
    return True             # This is cleaner, but, having we return only true or false, we can only                           evaluate the expression, and get the same result
  return False
print(is_even(51))


def is_even(number):        # Final, cleanest version
  return number % 2 == 0

print(is_even(50))




