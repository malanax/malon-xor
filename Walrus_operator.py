# Let's say we have a condition and wee need to assign a value in that condition. For that we use the Walrus operator:  ':='

tex = 'Hellooooo000'


if len(tex) > 10:
  print(f'Text has {len(tex)} characters')

# instead of calculating length 2 times, we can do:
# we asign the length to n while conditioning. For that we use ':='

if (n := len(tex)) > 10:              
   print(f'Text has {n} characters')


while ((n := len(tex)) > 1):    # cat timp lungimea lui tex e mai mare ca 1
  print(n)              # printam lungimea lui tex
  tex = tex[:-1]        # Micsoram lungimea lui tex cu 1 la fiecare iteratie
  # tex = tex[:-2] 
  # tex = tex[:-3] 