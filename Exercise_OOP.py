#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Kitty1', 4)
cat2 = Cat('Kitty2', 8)
cat3 = Cat('Kitty3', 6)


# 2 Create a function that finds the oldest cat
def oldest(*args):
  return max(args)

    


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest(cat1.age,cat2.age,cat3.age)} years old")





class C:
  def __init__(self, age, eye_color):
    self.age = age
    self.eye_color = eye_color
  
child1 = C(6,'Blue')
child2 = C(5,'Yellow')
child3 = C(10,'Brown')

def oldest(*args):
  return max(args)

def eyes(*args):
  for i in args:
    if i.age == oldest(child1.age,child2.age,child3.age):
      return i.eye_color



print(f'The oldest is {oldest(child1.age,child2.age,child3.age)} and has {eyes(child1,child2,child3)} eyes')