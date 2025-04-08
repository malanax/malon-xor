import re    # package for regular expressions

sir = 'I am living, you are living'

search = re.search('living', sir)  # returns a re object with the indexes of beggining                                      and end of the searched item

# (If the searched item isn't found, None is returned)

print(search)
print('')

print (search.span())   # a tuple of the indexes
print (search.start())  # the beggining index
print (search.end())    # the end index
print('')


# We can do a pattern, which can be used every time.

pattern = re.compile('living')

print (pattern.findall(sir))
print (pattern.search(sir))    # finds only the first encounter
print (pattern.fullmatch(sir))  # return false if the pattern is not exactly the same as the string we're looking into
print (pattern.match(sir))      # this one finds the match starting from index 0. So it must start the same