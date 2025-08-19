from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.shape("classic")
tim.color("brown")

# # Drawing a square with turtle
# for i in range (4):
#     tim.forward(100)
#     tim.right(90)

# # Draw a dashed line
# tim.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
colors = ["red1","red2", "green", "salmon", "purple", "linen", "gray", "gold"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):    
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    tim.color(choice(colors))


screen = Screen()
screen.exitonclick()