# fruits = ["Apple", "Banana", "Carrot"]
# #  access each item one by one and print each item
# for fruit in fruits: # each time the item is taken from the list and get stored in the variable named fruit for each item in the list
#     print(fruit)
#     print(fruit + " pie ")

# print the sum of marks of each subject 
marks = [80, 90, 81, 55, 20, 55, 99]

# using inbuilt python function for sum
subtotal = sum(marks)
print(subtotal)

# using manual method for sum
sum = 0
for score in marks:
    sum += score
    percentage = (sum/700)*100
    rounded_off_to_3_digit = round(percentage, 3)


print(f"The total percentage you obtained is {rounded_off_to_3_digit} and your total marks is {sum}")