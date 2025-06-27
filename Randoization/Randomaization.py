import random

random_integer = random.randint(1,10) # returns random whole number from 1 to 10
print(random_integer)

print(random.random())# returns int form 0.0 to 0.99999999 more than 0 less than 1
print(random.random()*10) # can use to randomize number from 0 to less than 10

print(random.uniform(1,3))# to create a random floating number including the numbers provided as parameters