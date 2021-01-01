import turtle as t
import random

snappy = t.Turtle()

snappy.shape("turtle")
snappy.pensize(15)
snappy.speed("fastest")
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r , g , b)



def randomWalk():

    directions = [0 , 90 , 180 , 270]

    snappy.color(randomColor())

    snappy.setheading(random.choice(directions))
    snappy.forward(30)
    
for _ in range(200):
    randomWalk()

screen = t.Screen()
screen.exitonclick()




