# putting one list/dictionaries into one
""" sample structure of nesting
{ 
list = []
dictionaries = {"keys":"values"}
}
"""
# example
fav_food = {
    "vegetable" : "cauliflower",
    "fruit" : "pineapple",
    "snacks" : "momo",
}

# nesting the dictionariies and list to store multiple vlaues in a single key

food_i_like_to_eat = {
    "vegetables" : ["cauliflower", "cabbage", "bringal"],
    "fuits" : ["apple", "oranges", "dragonfruits"],
    "snacks" : ["momo", "wings", "noodles"]
}

# printing oranges frrm fruits
 
print(food_i_like_to_eat["fuits"][1])

# nested list
new_nested_list = ["a", "b", "c", ["d","e","f"]]
print(new_nested_list[3][1]) # this prints "e"

# nesting a dictionary within a dictionary
new_nested_dictionary = {
    "places_visited" : {
        "Nepal" : ["Kathmandu", "pokhara"],
        "India" : "Delhi",
    },

}

print(new_nested_dictionary["places_visited"]["Nepal"][0]) # this should print Kathmandu as an input