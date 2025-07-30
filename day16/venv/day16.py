from prettytable import PrettyTable
import coffee_maker
import main
import money_machine


table = PrettyTable()
table.add_column("Pokemon Name" , ["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
#challenge was done
table.align = "l" #cause this is an attribute, here i changed the attribute
table.border = 0
table.border = 1


print(table)
