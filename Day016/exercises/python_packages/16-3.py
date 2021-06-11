from prettytable import PrettyTable

#object table
table=PrettyTable()


#printing pokemons and their types
#by building tables manually

#using add_column() method of  object table
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

#using attributes of  object table

#to align table to left,we use align attribute and  set it to "l"
table.align="l"




print(table)