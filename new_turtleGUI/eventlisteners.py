from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def move_backwards():
    tim.backward(10)

    
screen.listen()
screen.onkey(key = "w", fun = move_forward) # using functoin as input and we only add the name and not the paranthesis
screen.onkey(key= "a" , fun = turn_left)
screen.onkey(key= "d" , fun = turn_right)
screen.onkey(key= "s" , fun = move_backwards)
screen.onkey(key= "x" , fun = clear_screen)
screen.exitonclick()

# Higher order function: A function that takes other function as an arument or returns a function as its output

# An event listener is something that waits for a specific event to happen — like a click, key press, mouse movement, or custom trigger — and then runs a function (called a callback) when that event occurs.

# In Plain English:

# Think of it as saying:
# "Hey program, when this thing happens, please run that function."