
# We take a number and return the fibonnaci number in that index.

def my_gen(number):
  for i in range(number):
    yield i



def fib(number):
  
  # Facem fibonnaci
  num1 = 0
  num2 = 1

  for i in my_gen(number):
    yield num1
    temp = num1
    num1 = num2
    num2 = temp+ num2


for i in fib(20):
  print (i)
  # Iteram de number ori si returnam valoarea respectiva
