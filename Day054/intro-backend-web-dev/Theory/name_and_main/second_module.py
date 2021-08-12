#Now if you run this,output will be:
#First module's name:first_module
#Run from import

#This is because file is not being directly run,it is being imported.
import first_module



#This will be __main__ as python is running this file directly.
print(f"Second module's name:{__name__}")
