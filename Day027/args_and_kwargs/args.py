# Unlimited arguments
#eg. to add more than 2 numbers

def add(*args):
    #to display all arguments passed
    for n in args:
        print(n)

    #can also display argument at particular position
    print(args[2])

    s=0
    #printing sum using a loop
    for n in args:
        s=s+n       
    print(f"Sum is {s}")

    #printing their sum directly
    print(f"Sum is {sum(args)}")

    
add(5,3,4,8)

