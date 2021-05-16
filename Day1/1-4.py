#switch values of variables
a=input("a:")
b=input("b:")
#direct swap using 2 variables(more pythonic)
#a,b=b,a

#swapping using third temporary variable
c=a
a=b
b=c 
#print swapped values
print("a:"+a)
print("b:"+b)