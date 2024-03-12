import turtle as t
import random

tim = t.Turtle()

colors = ["green", "pink", "blue", "red", "snow4", "purple", "skyblue", "seagreen"]

direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))