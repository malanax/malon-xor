# Scope - what variables do I haave acces to?

def my_f():
  x = 10
  


#print(x)     this gives an error because x is defined inside the function, so it                    cannot be accessed outside of it

# if a variable is defined in a function, then it can be accessed only inside of it
# the above is called functional scope. When creating a function, we create a separate universe
# if a variable is defined in a general scope, it can be accessed anywhere

# Scope doesn't apply to conditional loops:

if True:
  x = 10

print(x)      # we can see we can use the variable created inside the loop
print('')



# Scope rules:
  # 1. Local Scope
  # 2. Parent scope
  # 3. Global scope
  # 4. built in functions

y = 1

def f():
  y = 11
  return y

print(y)        # This prints the variable from the general scope
print(f())      # This prints the altered variable from the function



def f():
  y = 11
  return y

print(f())    # Doing it like this, still doesnt alter the genreal scope Y because the                 altered y is available only for the functional scope
print(y)        
print('')


y = 1

def parent():
  y = 12
  def child():    # checks the local scope (child hasn't a y defined), so checks the                     upper level and finds y = 12
    return y      # returns that
  return child()  # returns what child returns by calling the child function

print(y)
print(parent())
print('')


# if, let's say we don't alter y inside the function, then the variable is returned as it is in the Global scope

y = 15

def func():
  return y

print(func())
print('')



# For the 4th rule we have the following example

def par():
  def child():
    return sum    # checks child() and finds nothing, checks par() and finds nothing,                  then checks the Global scope and finds nothing. Then, finally                      checks in built-in python has something and returns that
  return child()
print(par())


# GLOBAL keyword - for using a global variable. define it with global.
# we want to make a counter function

total = 0

def counter():

  #total += 1        this can't be used because total is not recognized

  global total      # We take the total variable from the global scope
  total+=1          # increment it with 1

  return total      # return the value

print(counter())
print(counter())
print(counter())
print(counter())    # returns 4
print(total)       # we see by printing the global variable that it's now 4
print('')



z = "Text misto"

def f():
  #z = 0 
  global z
  return z

print(f())

# GLOBAL keyword is not the best way to do things due to confusions that may be created by acessing scopes from everywhere. So we have the best way here:

z = 0       

def counter(total):
  total+=1
  return total

print(counter(counter(counter(z))))  # returns 3
print(z)   # z never gets changed


# NoNLOCAL - Takes a variable that's nonlocal but it's not global. ex from a parent
# also non-advised. Good in some situations

def outer():
  s = "hey"           # modifies this nonlocal variable
  def inner():
    nonlocal s
    s = "Hello"
    print('inner: '+s)
  inner()
  print('outer: '+ s)
  
outer()


#       Scope is useful because we have limited resources. After a function is used, the memory it uses is freed so other things can use it. That data is destroyed
  # So, use functions if you want to use less memory when programing