is_old = True
is_licensed = True

# IF block

if is_old:          # is_old evaluates to True; if is_old is true
  print("Old enough to drive")    # then print the text
print('checkcheck')

  # Syntax:  if condition:
  #            instructions

  # Indentation is important. It serves as {} in other languages
  # For example, print checkcheck from above doesn't enter the if Block

print('\n')

# if we change is_old to false, we'll see that checkcheck still prints

is_old = True

if is_old:                       # is_old is not True so the instructions don't execute
  print("old enough to drive")
print('checkcheck')              # and this gets printed because it's out of the                                          condition
print('\n')



if is_old:                       # if is_old is true then execute the conditions bellow
  print("old enough to drive")
else:                            # else, if it's false, execute the conditions bellow
  print('checkcheck')
print('\n')



if is_old:                       # if is_old is true then execute the conditions bellow
  print("old enough to drive")
elif is_licensed:                # else, if is_licensed is true, execute the below
  print('You can drive now!')
else:                            # else, if both are false, execute the bellow
  print('checkcheck')
 
print('\n')

# The condition is an expression. An expression is something that produces a value
# So we can do

if is_old and is_licensed:      # if is_old is true and is_licensed is true, execute
  print("Good to drive!")
else:
  print("Access not granted")
print('\n')




# Let's say we change the parameters to other type than boolean
is_old = "Yes"
is_licenced = 5

if is_old and is_licenced:     # Python automatically convertes to boolean, so both                                     are TRUE, see bellow an illustration
  print("Go")
else:
  print('No')

is_old = bool('Yes')
is_licenced = bool(5)

print(is_old)              # they both return True -> this is considered TRUTHY
print(is_licenced)


is_old = bool('')          # in general, empty values of datatypes are considered                                   Falsey, including None, decimals, fractions
is_licenced = bool(0)

print(is_old)              # they both return False -> this is considered Falsey
print(is_licenced)


# Truthy and Falsey are useful when checking if a form has been completed for ex:
# or if a variable has a value
username = 'ndkjanf'
password = '123'

if username and password:
  print('User registered')

print('\n')



# Ternary operator -> shortcut for if
# Syntax: instruction_if_true if condition else instruction_if_false

print('below') if 2<5 else print('above')

  # Below is an example of populating a variable with a condition
is_friend = True
can_message = "message allowed" if is_friend else "can't message this one"
print(can_message)


age = 5
can_have_phone = "yes" if age>=12 else "No"
print(can_have_phone)


name = "Alex"
among_the_first = True if name.lower().startswith('a') else False
print("you've been called") if among_the_first else print("You must wait")
print('\n')


# Shortcircuit
  # It means that if for the "and" keyword, the first argument is False, Python doesn't read further and just doesn't do the instructions

if False and True:
  print("Prints and")

  # It means that if for the "or" keyword, the first argument is False or True, Python doesn't read further and just does the instructions

if True or False:
  print("Prints or")

 # It's valid only for booleans
n = 5
if n == 3 or n == 4:
  print('Got it')
else:
  print("The value isn't found")
print('\n')


                    # Logical operators

print(2 > 5)     # FALSE
print(2 < 5)     # TRUE
print(2 == 5)    # FALSE
print(2 != 5)    # TRUE
print('\n')

  # For letters

print('a' > 'b')   # False, the letters grow. A is the lowest, Z is the greatest
print('a' < 'b')
print('a' > 'A')   # Lower case letters are greater than Upper case letters
print('a' > 'B')
print('\n')

  # NOT negates the condition
print(not(True))
print(not(False))
print(not(2<5))
print('\n')


# Exercise:
is_magician = False
is_expert = True

if is_magician and is_expert:
  print('You are a master magician!')
elif is_magician and not(is_expert):
  print("At least you're getting there")
elif not(is_magician):
  print("You need magic powers")

print('\n')


# == sign converts both values into one of them to compare them.
# == compares the VALUE

print (True  == 1)
print ('' == 1)   # False
print ([] == 1)   # False
print ( 10 == 10.0)
print ([] == [])
print('\n')


# 'is' checks if the location in memory is the same. So the below will be false
# 'is' compares the exact location
print (True  is 1)
print ('' is 1)   
print ([] is 1)   
print ( 10 is 10.0)
print ([] is [])

print( True is True)  # this will be true
print('1' is '1')     # this will be true
print([] is [])       # this will still be false because every list is created                                 SOMEWERE ELSE IN MEMORY
# Every datastructure is created SOMEWERE ELSE IN MEMORY



                          