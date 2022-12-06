a = {1,2}
a.add(4) 
a.add(4)
a.add(4) # adding value repeatedly cannot chnage set
print(a)
a.add((1,))
print(a)

## You cannot add list/Dictionary to the sets
print(len(a)) # print the length of the set
a.remove((1,)) #remove {tuple(1,)} from the set
print(a)
a.pop() # to remove the random element from the set
print(a)
a.clear() # to clear the set
print(a)
print(a.union({1,2,5})) # for union
print(a.intersection({7,88,7})) #for intersection
