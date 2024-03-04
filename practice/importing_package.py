from prettytable import PrettyTable
table = PrettyTable()
print(table)
#creating the table using prettytable package
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)