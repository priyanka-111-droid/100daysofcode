def format_name(first_name, last_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if first_name == "" or last_name == "":
    return "You didn't provide valid inputs."

  return f"Result: {first_name.title()} {last_name.title()}"



#after replacing function call,the name is stored in variable storing_returned_name
storing_returned_name=format_name(input("Your first name: "), input("Your last name: "))
print(storing_returned_name)

#can also use print directly WITHOUT storing in another variable,gives same result....
print(format_name(input("What is your first name? "), input("What is your last name? ")))
