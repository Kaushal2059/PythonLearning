def leap_year(year):
    """ take a year as an argument and print if the year is a leap year or not """ # this is an example of docstring
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return f"the year {year} is a leap year"
    elif year % 4 == 0 and year % 100 != 0:
        return f"the year {year} is a leap year"
    else:
        return f"the year {year} is not a leap year"
is_done = True
while is_done:
    is_leap_year = leap_year(int(input("Enter the year you want to check: ")))
    print(is_leap_year)
    done = input("are you done type 'yes' or 'no'").lower()
    if done == "no":
        is_done = False
        print("thanks for using my program!")


