class PlayerCharacter:  # Declaring a class

    membership = True  # Class object attribute. Static. The same                                             for every object created with this class

    def __init__(
        self, name, age
    ):  # Creating __init__ method. This is a                                                  Constructor
        if PlayerCharacter.membership == True:
            self.name = name  # Takes the name given and atributes it to the                                     object. Dynamic
            self.age = age

    def run(self):  # defining a run() method
        #print('RUN')
        return 'RUN!'

        # self is always the first parameter in a class's method


player1 = PlayerCharacter('Alex',
                          26)  # instantiating the class. Object player1
player2 = PlayerCharacter('Denis', 24)

print(player1)
print(player1.name)
print(
    player2.run()
)  # None is displayed after RUN because the function doesn't                               return anything

print(
    player1.membership
)  # For the class attribute, we can see it;s the same for                                   both
print(player2.membership)

# Although the objects are using the same blueprint to be created, the objects are created in different locations in memory
print(player1)
print(player2)

# We can create attributes outside of the class..not really:

#player1.attack = 50
#print(player1.attack)
#print('')

# We can use the help function to see what 'magic methods'(__meth__) we have available for the class or any datatype

#help(PlayerCharacter)
#help(list)

# If we want to use a paramater from another function inside the class, we need to use 'self'


class Client:
    def __init__(self, name):
        self.name = name

    def naming(self):
        #print(name)       # this gives an error
        print(self.name)  # this is how it's done


client1 = Client('Bambina')
client1.naming()

#        __init__  ->  Constructor

# It gets called every time we instantiate


class Incercare:
    def __init__(self, name="Bam", age=0):  # default param
        if age > 18:  #Because age is 0 by default, the object                                      doesn't instantiate, doesn't enter this condition
            self.name = name
            self.age = age


#incercare1 = Incercare()
#print(incercare1.name)

incercare2 = Incercare('Ale', 23)
print(incercare2.name)

# @classmethod - @staticmethod


class Incercare:
    def __init__(self, name="Bam", age=0):
        if age > 18:
            self.name = name
            self.age = age

    @classmethod  # class method - can access class's atributes
    def adding_things(cls, no1, no2):  # it uses cls instead of self
        return no1 + no2

    @staticmethod  # static method - can't access anything in the                                         class. Just a normal method
    def adding_things2(no1, no2):
        return no1 + no2

    def cinfo(
        self
    ):  # instace method - can access the _init_ params                                        and class atributes
        return self.name, self.age


inc2 = Incercare("ha", 23)
#print(inc2.adding_things(2,3))

print(
    Incercare.adding_things("he", "llo")
)  # it's a method that can be used without                                                 instantiating the class
print(inc2.adding_things2(1, 2))

print(inc2.cinfo())

#Instance Methods: The most common method type. Able to access data and properties unique to each instance.

#Static Methods: Cannot access anything else in the class. Totally self-contained code.

#Class Methods: Can access limited methods in the class. Can modify class specific details.




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
