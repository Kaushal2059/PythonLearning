import turtle as t 
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("triangle")
tim.color("brown")
# tim.pensize(15)
tim.speed("fastest")

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_circle(num_of_gap):
    inrange = int (360/ num_of_gap)
    for _ in range(inrange):
        tim.color(randomcolor())
        tim.circle(150)
        tim.setheading(tim.heading() + num_of_gap)

draw_circle(0.1)
       
screen = Screen()
screen.exitonclick()