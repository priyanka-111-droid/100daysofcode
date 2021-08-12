def error_handler(original_function):
    def wrapper_function(*args,**kwargs):
        try:
            x=original_function(*args,**kwargs)
        except Exception as e:
            print(f'Exception:{type(e).__name__}')
            print(f'Exception in {original_function.__name__ } function')

    return wrapper_function

@error_handler
def divide(a,b):
    print(a/b)

@error_handler
def key_of_dictionary(a_dictionary,non_existent_key):
    value=a_dictionary[non_existent_key]
    print(value)

@error_handler
def element_of_list(fruit_list,index):
    print(fruit_list[index])

@error_handler
def string_and_int(text,number):
    print(text+number)

#Now testing if errors are being detected(name of error and print name of function where error detected)
divide(20,0)
key_of_dictionary( {"key":"value"},"key2")
element_of_list(["apples","bananas","oranges"],4)
string_and_int("abcd",5)



