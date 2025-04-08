from collections import Counter, defaultdict, OrderedDict

l1 = [1,2,3,3,3,4,5,6,6]
sentance = "What's up? Imma play with you!"


counter_li = Counter(l1)     # Counter object
counter_st = Counter(sentance)


print(counter_li)            # prints a list which states how many times each item appears
print(counter_st)            # counts how manny times each item appears in the string
print('')



# defaultdict

dictio = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2})  # lambda is a default value we pass so it takes over when something that does not exist is called

print(dictio['d'])
print('')

# OrderedDict      #################    Python has made dictionaries ordered by default

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1


print(d==d2)           # This is false because the order of the elements is not the same
