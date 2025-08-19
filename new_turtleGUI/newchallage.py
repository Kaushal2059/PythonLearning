# import colorgram 

# rgb_colors = []
# colors = colorgram.extract('new_turtleGUI/image.jpg', 6)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t 
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

color_list = [(181, 171, 162), (211, 208, 204), (220, 224, 229), (226, 219, 222), (219, 226, 222), (208, 195, 163)]

tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def make_dots(num):
    for _ in range(num):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

for _ in range(10):
    make_dots(10)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    

screen = Screen()
screen.exitonclick()