import copy
l=[1,2,3,4,5]
dup=copy.deepcopy(l)
print(l)
print(dup)
print('---------------')
print(id(l))
print(id(dup))
print('---------------')
print(l is dup)
print(l[0] is dup[0])
print('---------------')
l[1]=3
print(l)
print(dup)
