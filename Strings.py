import datetime

prop = "Its kind of sunny outside. Take care!"
print(prop)

prop_re = "\t It\'s \"kind of\" sunny outside.\n Take care!"
print(prop_re)

#String formatting
name = "Viktor"
age = 30

prop = "Hi " + name + '. You are ' + str(age) + " years old."
print(prop)

#Formatted version
print(
    f"Hi {name}. U are {age} years old."
)  #Note: formatted string has an 'f' at the                                                   beggining - THIS IS THE WAY TO GO

#OR
print("Hi {}. Your age is {}".format(name, age))
#We can take them by whatever order
print("Hi {1}. Your age is {0}".format(name, age))
#We can declare variables while doing this
print("Hi {name_new}. Your age is {age_new}".format(
    name_new="Mike", age_new=44))  # --THIS IS OLD

s = "my name is {}".format(name)
name2 = "Mira"
print(f"Hi, {name2} " + s)
print("dude")
print("And that's that!")

lista = ['harry', 'dani', 'Maria', 'INdia']

for i in lista:
  if (i[1].isupper()):
    print(
        str(lista.index(i)) + " - " + lista[lista.index(i)]
    )  #prints the name with the                                                                upper second letter

# INDEXES
selfish = "me me me"
#  01234567

print(selfish[0])  # appealing a string index
print(selfish[0:4])  #appealing a string index range
#items 0-3
print(selfish[0:8:3])  #from 0 to 7, 1 by 3
print(
    selfish[1:]
)  #all the elements starting from the                                                          second
print(
    selfish[:5]
)  #all the elements 'til index 4 or                                                            'til the fifth element
print(selfish[::1])  #all the elements
print(selfish[::2])  #all the elements 1 by 2
print(
    selfish[-1]
)  #negativ indexes start from the end                                                          of the string
print(selfish[::-1])  #reverse of the string :DDD

#-----IMMUTABILITY of strings
#-can't reasign a part of the string
#-must reasign the hole variable

prop = "yow yow! wassap?"
print(prop)
print(prop.upper())  #self-explanatory methods
print(prop.capitalize())

print(
    prop.find("wassap")
)  #prints the starting point index of the                                                      searched word
print(prop.replace("yow", "Ba!"))  #replaces the 1st with the 2nd
print(prop.replace("yow", "Ba!", 1))  #the same, but 1 time
#this will not change the original string due to immutability, REMEMBER!
print(prop)
prop = prop.replace("yow", "ba")  #this is how we change the original
print(prop)

#BOOLean
car = "Ferrari"
is_sweet = True

if (car == "Ferrari"):
  print(is_sweet)
else:
  is_sweet = False
  print(is_sweet)

######  This splits the text in lines of 2
import textwrap

striing = "ABCDEFGHIJKLMNOPQRSTU"
max_len = 2

print("\n".join(textwrap.wrap(striing, max_len)))
#######

#Exercise
birth_year = int(
    input("What year were you born in?\n")
)  #input() collects an input as a                                                                string
this_year = datetime.datetime.now().year
age = this_year - birth_year

print(f"your age is {age}")

#Exercise 2
username = input("Enter an username:\n")
password = input("Enter a password:\n")

password_length = len(password)
covered_password = "*" * password_length

print(
    f"{username}, your password {covered_password} is {password_length} letters long. :D"
)

#----OR we can use the "len" method inside the formatted string:
print(f"{username}, your password is {len(password)} letters long.")
