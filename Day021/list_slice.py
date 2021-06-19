#Demo of list slicing and tuple slicing
#index of first element is 0

piano_keys=["a","b","c","d","e","f"]

print(piano_keys[2:5])   #['c','d','e']

print(piano_keys[2:])    #['c', 'd', 'e', 'f']

print(piano_keys[:5])    #['a', 'b', 'c', 'd', 'e']

print(piano_keys[2:5:2])  #['c', 'e']

print(piano_keys[::2])    #['a', 'c', 'e']

print(piano_keys[::-1])   #['f', 'e', 'd', 'c', 'b', 'a']



#also done with tuples
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])


