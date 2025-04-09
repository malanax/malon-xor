#                     1. Encapsulation

# encapsulation of the data in one package (the class), a data that has meaning
# both methods and atributes

class Man():
  strength = 0
  build = "tiny"

  def __init__(self, strength = 1, build = "small"):
    self.strength = strength
    self.build = build

  @classmethod              
  def show_male(cls):
    return cls.strength, cls.build
  
  @staticmethod
  def m(strs = 2):
    return strs

  def meth(self):
    return self.strength

man1 = Man(10, "solid")
man2 = Man()

# The below refers to the python methods: class, static and instance
print(man1.show_male())         # returns class atributes
print(man2.m())                 # returns method's atributes
print(man1.meth())              # returns object's atributes
print('')






#                        2. Abstraction

# Is the process where we take only what we need from a class.





#       Public & Private

# There's no public and private in Python, but there's a convention that for 'private' variables we should use '_' like this : _name, _age. Ex:

class Pilot():
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  def print_info(self):
    print(f"I am {self._name} and I am {self._age} years old.")

pilot1 = Pilot("Bogdan", 32)
pilot1.print_info()
print('')







#                           3. Inheritance

# Is when we inherit from other class. Syntax: we declare another class with the class we inherit from in the paranthesis.

class User():
  def sign_in(self):
    return 'Succesfully signed in!'

  def attack(self):
    return 'Do nothing'


class Wizard(User):
  def __init__(self, name, power):
    self._name = name
    self._power = power

  def attack(self):
    return f'Wizard {self._name} attacks with {self._power} power!'
  

wizard1 = Wizard('Merlin', 90)
print(wizard1.attack())


class Archer(User):
  def __init__(self, name, arrows):
    self._name = name
    self._arrows = arrows
  
  def attack(self):
    return f'Atcher attacks with arrows. Arrows left: {self._arrows}'


archer1 = Archer('Robin', 100)
print(archer1.attack())

print(wizard1.sign_in())               
print(archer1.sign_in())

 # both subclasses can access the User's sign_in method, as User() is the parent class and Wizard() and Archer() are the children

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

# If a class is used with () Python expects to instantiate it. If you want to use the clase in a method without instantiating it, use it without ()


print(isinstance(wizard1, object))  # every class iherits from the object class







#                        4. Polymorphism

# a function with the same name does different things based on the object calling it

# We have the upper classes..

# First way to ilustrate polymorphism:

def player_attack(player):
  return player.attack()

print(player_attack(archer1))
print(player_attack(wizard1))

# Second way:

for i in [wizard1, archer1]:
  print(i.attack())




#   super()


class Paran():
    def __init__(self, mail):
        self._mail = mail

    def get_mail(self):
        return self._mail


class IsParan(Paran):
    def __init__(self, mail):
        super().__init__(mail)

    def has_mail(self):
        has = "has mail"
        has_not = "doesn't have mail"

        if Paran.get_mail(self) != '':
            return has
        else:
            return has_not


client = IsParan('')
print(client.has_mail())
print('')





# Instrospection

print(dir(client))    # allthe methods of the instance
print('')



#                             Dunder Methods

# Dunder methods represent the built in functions of python

class Dog():
  def __init__(self, color):
    self._color = color
    self._my_dict = {
      "name": "yoyo",
      "age" : 15
    }
  
  def __str__(self):                      # __str__ represents str
    return f"This dog is {self._color}"

  def __call__(self):                     # __call__ represents when the object is                                              called
    print("Called!")

  def __len__(self):                      # __len__ represents len
    return 6

  def __getitem__(self, i):               # __getitem__ represents when we call a index
    return self._my_dict[i]


doberman = Dog("black")

print(doberman.__str__())   # The same
print(str(doberman))
doberman()

print(len(doberman))        # we can see here that the override is valid only inside                                 the class
print(len([1,2,3]))

print(doberman['name'])     # using the __getitem__ dunder function
print('')






#                         Multiple Inheritance

class User():
  
  def signed_in(self):
    print('signed_in')

class Wizard(User):
  def __init__(self, name, power):
    self._name = name
    self._power = power
  
  def attack(self):
    return f"{self._name} attacks with {self._power} power!"


class Archer (User):
  def __init__(self, name, arrows):
    self._name = name
    self._arrows = arrows
  
  def attack(self):
    print (f'{self._name} attacks with arrows!')
    return f'{self._arrows} Arrows remaining'



  def run(self):
    return "Archer runs!"


#----



class MergedCyborg( Wizard, Archer):      # if there are common methods, the method                                                from the first mentioned class is used, so                                             we do:
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)
  

cyborg = MergedCyborg("Robocop", "Infinite blast", 1000)

print(cyborg.attack())
print(cyborg.run())
print(cyborg.signed_in())

