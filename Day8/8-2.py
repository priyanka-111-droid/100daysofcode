
def prime_check(num):
    #METHOD 1:using counter
    # counter=0   #counts how many numbers num is divisible by(factors of num)
    # for x in range(1,num+1): 
    #     if(num%x==0):   #if num is divisible by x leaving no remainder,x is a factor of num
    #         counter+=1

    # if(counter==2):  #if num has two factors-1 and itself,it is prime
    #     print("It's a prime number.")
    # else:
    #     print("It's not a prime number.")

    #METHOD 2:using boolean flag(set it to True and False depending on condition)
    is_prime=True #initially set flag is_prime to true
    
    for i in range(2,num):#for loop from 2 to num-1 as range for loop ends at num-1
        #since num itself and 1 are not included in this loop
        if(num%i==0):
            #if num is divisible by any number,it will not be prime anymore
            is_prime=False  #set flag to false

    if is_prime: #can also be written as is_prime==True
        print("It's a prime number.") 
    else:
        print("It's not a prime number.")

n=int(input("Enter a number"))
prime_check(n) 

#REMEMBER
# is_prime condition is checked OUTSIDE for loop so make sure of the indentation