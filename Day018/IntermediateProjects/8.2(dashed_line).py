from turtle import Turtle

snappy = Turtle()

snappy.shape("turtle")
snappy.color("seagreen")

for _ in range(15):
    snappy.forward(10)
    snappy.penup()
    snappy.forward(10)
    snappy.pendown()