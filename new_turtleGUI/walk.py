import turtle as t 
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("triangle")
tim.color("brown")
tim.pensize(15)
tim.speed("fastest")

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


direction = [90, 180, 270 , 0]

for _ in range(100):
    tim.forward(50)
    tim.setheading(random.choice(direction))
    tim.color(randomcolor())
  
screen = Screen()
screen.exitonclick()