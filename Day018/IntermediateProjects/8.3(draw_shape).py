from turtle import Turtle,Screen
import random

colors = ["medium blue","firebrick","pink","violet","green yellow","green","orange","brown"]


snappy = Turtle()

snappy.shape("turtle")

def drawShape(n_sides):
    color = random.choice(colors)
    snappy.pencolor(color)

    angle = 360/n_sides

    for _ in range(n_sides):

        snappy.forward(100)
        snappy.left(angle)

for i in range(3,10):
    drawShape(i)
    
screen = Screen()
screen.exitonclick()