# Dictionaries
# has key and value enclosed under "" as dictionary = {"key" : "value"}

new_dictionary = {
    "Name":"Kaushal",
    "nationality":"Unknown",
    "gender":"must be a male",
}

print(new_dictionary["Name"])
                
new_dictionary["works_on"] = "nowhere" # adding a new key value pair in the existing dictionary
print(new_dictionary)

empty_dictionary = {} # creating a new empty dictioary

# wiping out n entire dictionary
# new_dictionary = {}
# print(new_dictionary)

new_dictionary["works_on"] = "freelance"  # editing an existing key value pair
print(new_dictionary)

# looping through a dictionary
for something in new_dictionary:
    print(something) # this will print all the keys of the dictionary
    print(new_dictionary[something]) # this will print the value based on the keys fetched