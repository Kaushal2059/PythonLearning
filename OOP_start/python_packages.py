from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["kaushal","Hari","Sita"]),
table.add_column("Address", ["Naikap", "Thankot", "Lalitpur"])
table.align = 'l'
print(table)