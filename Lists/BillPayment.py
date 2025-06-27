import random
Names = input("Enter the peoples who are present seperated by space:\n")
mylist = Names.replace(","," ").split() # this will replce all the commas into whitespaces and also more than one white space will be treated as a single white spaces because of the split function and this will also convert user input into list
#option 1
length_of_string = len(mylist)
index_of_payee = random.randint(0,length_of_string - 1)
print("The lucky charm to pay todays bill is",mylist[index_of_payee])
#option 2
print("the one to pay the bill is ", random.choice(mylist))