def format_name(first_name,last_name):
        # print(first_name.title())
        # print(last_name.title())

        #printing on same line with space between
        #print(f"{first_name.title()} {last_name.title()}")

        #returning this will replace function call
        return f"{first_name.title()} {last_name.title()}"
            
#after replacing function call,the name is stored in variable storing_returned_name
storing_returned_name=format_name("mArY","SmITh")
print(storing_returned_name)

#can also use print directly WITHOUT storing in another variable,gives same result....
print(format_name("mArY","SmITh"))

