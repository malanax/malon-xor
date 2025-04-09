# We can do it with try: except
#a = True
#while a:
 # try:
  #  age = int(input("Enter your age: "))
   # print (age)
    #a = False
  #except:
   # print("Please enter a number.")




# Instead of changing the condition of while to break the loop, we can do:

while True:
  try:
    age = int(input("Enter your age: "))
    result = 10/age
    print (result)
  except ValueError:          # we catch only the ValueError. Other errors are not                                   catched here.
    print("Please enter a number!")

  except ZeroDivisionError:   # we catch the Zero Division error. Same as above
    print("Please enter a number greater than 0!")
                              # we catch this errors separately because we need another message to display depending on the error
  else:                       # else is for except. If an error is not found, then:
    print('Thank you!')       # We thank the user for the input
    break                     # We break the loop, because we have what we need
  finally:                    # finally executes at the end of the block no matter wht
    print('Finally!')


print('')

# We have a sum function. Let's handle the errors:


def sum(n1,n2):
  try:
    return n1/n2
  except (TypeError, ZeroDivisionError) as err:   # we can handle more errors at a time
    print(f'Please pass only numbers! Make sure they are not 0! {err}')

   
print(sum(1,10))
