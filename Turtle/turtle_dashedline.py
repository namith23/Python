from turtle import Turtle,Screen

line = Turtle()
line.shape("arrow")
for _ in range(15):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()



screen = Screen()
screen.exitonclick()