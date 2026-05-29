
# Example of list comprehension
list = [10,20,2,30,4]

new_list = [n+1 for n in list]
print(new_list)

# Example 2 string
string = "Kaushal"
New_string = [letter for letter in string]
print(New_string)

# example 3
list = [item*2 for item in range(1,5)]
print(list)

#Conditional list_comprehension
names = ["Kaushal","Hari","Gita","Sita","Ram","Mandal"]
# short_names = [item for item in names if len(item) < 5]
# print(short_name)
Uppercased_name = [name.upper() for name in names if len(name) > 5]
print(Uppercased_name)

# Example to convert to integer and print list of even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)