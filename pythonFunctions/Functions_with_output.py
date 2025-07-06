def product():
    result = 3 * 10
    return result

output = product()
# print(output)

def format_name(f_name, L_name):
    formatted_first_name = f_name.title()
    formatted_last_name = L_name.title()
    return f"{formatted_first_name} {formatted_last_name}"

formatted_string = format_name("kaushal","Rupakheti")
print(formatted_string)
print(format_name("RaM","ShreSTha")) # both of the ways of printing output are correct

# Differece between using return and using print directly
# The 'return' is te end of the funtion nothig written after that will ever be executed
# you cannot have a mutiple return keyword inside a same function

def city_name(country, city):
    if country == "" and city == "":
        return #this will terminate the functions if the condition matches and the rest of the code will not be executed
    country_name = country.title()
    city_name = city.title()
    return f"{country_name} {city_name}"
    
# Last_visited_place = city_name(input("Enter the country you visited", input("Enter the name of the city")))
print(city_name(input("Enter the country you visited", input("Enter the name of the city"))))
