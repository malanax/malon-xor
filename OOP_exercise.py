class SuperList():
  def __init__(self, lis):
    self._lis = lis

  def __len__(self):
    counter = 0

    for i in self._lis:
      counter += 1
    
    return counter
  
  def __append__(self, item):
    self._lis = [self._lis,item]
    return self._lis
  
  def __getitem__(self, i):
    return self._lis[i]

my_list = SuperList([1,2,3,4,5])

print(my_list.__len__())

print(my_list.__append__(2))
print(my_list.__len__())

print(f"First {my_list[0]}")
print(f"Second {my_list[1]}")
print('')


# or simpler we inherit from list

class SuperList1(list):
  def __len__(self):
    return 1000

l1 = SuperList1()
print(len(l1))

l1.append(2)
l1.append(3)
l1.append(4)
print(l1[0:2])
    



