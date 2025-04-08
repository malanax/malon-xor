li = [1,2,3,4,5]
li2 = ['a','b','c','d','e']
li3  =[1,'a',True,48.69]        #can contain any type

print(li)
print(li2)
print(li3)

print(li[0])                    #index starts from 0
print(li[1])
print('\n') 

amazon_list = [
  'computer',
  'screen',
  'speakers',
  'charger'
]

print(amazon_list[0:3:2])    #LIST SLICING
print(amazon_list[0::3])     #all elements with a step by 3
print(amazon_list[0:2:1])    #first 2 elements step by step
print('\n') 

amazon_list[0] = 'laptop'    #LISTS ARE MUTABLE
amazon2 = amazon_list[0:3]
print (amazon2)
print(amazon_list)
print('\n') 


#IMPORTANT TO KNOW
#if you want to copy a list to another variable, you need to do this
amazon3 = amazon_list[:]        #note the [:]
amazon3[0] = 'Mammoth'

print(amazon3)
print(amazon_list)
print('\n')                #you can see from the output that these are 2 different                                               lists

#if you just do this:
amazon3 = amazon_list           #then amazon3 will just be a refference to amazon_list. So every                                      change you make to amazon3, will be made to amazon_list, also
amazon3[0] = 'Mammoth'

print(amazon3)
print(amazon_list)  
print('\n') 

# MATRIX
# IN PYTHON, A MATRIX IS A MULTIDIMENSIONAL LIST
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[1][1])          #second row, second column
print('\n')


#LIST FUNCTIONS
#--- ADDING
basket = [1,2,3,4,5]
basket.append(100)         # 'append' adds an element to the end of the list.
new_basket = basket

print(new_basket)
print(basket)

basket.insert(1, 450)                   # 'insert' adds an element to the specified index                                     and shifts the element that was in that place to the right
print(basket)


basket.extend([25,50,75,100])         # 'extend' extinde lista existenta, adaugand lista                                            specificata la final
print(basket)


#--- REMOVING
popped = basket.pop()                    # 'pop' cuts the last element of the list and                                                returns it
basket.pop(0)                      # removes the item in the index

basket.remove(25)                       # 'remove' removes the value from the list

print(popped)
print(basket)


basket.clear()                  # 'clear' clears the list
print(basket)


ls = [90,80,70,60,50,40,30,20,10,80,80]

print(ls.index(80))      # prints the index of the element

alph = ['a','b','c']
print(alph.index('c'))

print(ls.index(60, 0, 4))   # searches in the given borders of 0 and 4

print('i' in "Hi")        # if the letter exists in the string, returns true.
print('x' in 'Hi')
print(ls.count(80))       # returns how many times it appears in the list

ls = [10,9,8,7,6,5,4,3,2,1]
ls.sort()                 # sorteaza crescator (modifica lista curenta)
print(ls)

ls=['e','d','c','b','a']   
ls.sort()                   # sorteaza
print(ls)

ls = [5,4,3,2,1]
print(sorted(ls))          # sorteaza, returneaza alta lista (nu modifica lista curenta)
print(ls)

new_list = ls[:]
print(new_list)
                                    # these 2 are the same
new_list = ls.copy()
print(new_list)

ls.reverse()              # reverses the list
print(ls)

basket=['a','b','c','d']
basket.reverse();
print(basket)
print(basket[::-1])      #slicing cretes a copy of the list
print(basket)

ranest = range(1,101)     
print(list(ranest))         #prints a list from 1 to 100. Stops before 101

print(list(range(101)))     #prints a list from 0 to 100. Begins at 0, stops before 101


#Combining lists into a string using join()

#syntax:  string.join(['','','','','']) <- as many aruments as you want
#scope:  joins any LIST ELEMENTS into a STRING

strings = ' '               # Every item in the list below joins whatever is in this string

new_string = strings.join(['Hi,', 'my', 'name', 'is', 'Alex'])    #this creates another string

print(new_string)

      # SAME AS

print(' '.join(['Hello,','this','is','separated','by','spaces']))
print('\n\n')

#LIST UNPACKING

a,b,c = ['1','2','3']     # a,b,c se populeaza cu 1,2,3
print(a)
print(b)
print(c)
print('\n')

a,b,c, *rest = [1,2,3,4,5,6,7,8,9,10]   # a,b,c se populeaza cu 1,2,3 iar rest se populeaza cu restul variabilelor. A se nota *
print(a)
print(b)
print(c)
print(rest)
print('\n')

a,b,c, *rest, d, e = [1,2,3,4,5,6,7,8,9,10]  # daca declaram si alte variabile dupa cea multipla, ele se vor popula automat cu elementele din coada
print(a)
print(b)
print(c)
print(rest)
print(d)
print(e)
print('\n')

# NONE este Null din alte limbaje
weapons = None
print(weapons)
print('\n')

if (weapons == None) :
 weapons = 2
 print(f"Ups, forgot to get the weapons. Now I have {weapons}")
