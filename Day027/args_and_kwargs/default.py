#Default arguments
def my_function(a=1,b=2,c=3):
    print(f"value of a is {a},b is {b},c is {c}")


my_function()       # So if we don't give values for a,b,c it will give default values.
my_function(b=5)    # We can also alter values for any one of them.


