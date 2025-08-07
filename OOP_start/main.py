from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

# TO demonstrate attributes
my_screen = Screen()
print(my_screen.canvheight)

# To demonstrate a method (method is a function associated with an object)
my_screen.exitonclick()