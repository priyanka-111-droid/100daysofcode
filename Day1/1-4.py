#switch values of variables
a=input("a:")
b=input("b:")
#METHOD 1:direct swap using 2 variables(more pythonic)
#a,b=b,a

#METHOD 2:swapping using third temporary variable,in this case,c
#Remember,assignment operator(=) assigns values on the right to the variable on its left
c=a  #value of a is stored in c
a=b  #value of b is stored in a
b=c  #value in c is now stored in b
#print swapped values
print("a:"+a)
print("b:"+b)
