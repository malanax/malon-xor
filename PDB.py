import pdb

input1 = int(input('Enter something: '))
input2 = int(input('Enter something: '))

def mult(a, b):
  #return a*b
  pdb.set_trace()
  return a+b

print(mult(input1, input2))


class Dog():
  def __init__(self, race, color, age):
      self._race = race
      self._color = color
      self._age = age

  def print_dog(self):
    print (self._race, self._color, self._age)

my_dog = Dog("Doberman", "black", 6)
my_dog.print_dog()
#Dog.print_dog(my_dog)