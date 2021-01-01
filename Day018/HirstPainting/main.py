# import colorgram

# rgb_colors = []

# colors = colorgram.extract("painting.jpg",30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append( (r , g , b) )

# print(rgb_colors)

import turtle as t
import random

snappy = t.Turtle()
t.colormode(255)
t.speed(1)
dot_count = 100

color_list = [(210, 156, 103), (108, 110, 128), (139, 141, 154), (235, 214, 226), (225, 214, 110), (186, 66, 29), (221, 236, 225), (206, 145, 175), (180, 159, 38), (102, 110, 174), (22, 23, 66), (199, 15, 3), (23, 43, 23), (228, 167, 197), (219, 80, 56), (36, 38, 15), (43, 45, 110), (232, 173, 161), (156, 170, 159), (199, 11, 21), (148, 67, 82), (212, 76, 99), (84, 101, 87), (180, 181, 218), (222, 208, 19), (42, 22, 42), (69, 73, 40), (46, 74, 50)]

t.hideturtle()
snappy.hideturtle()
t.speed("fastest")
snappy.setheading(255)
number_of_dots = 100
snappy.penup()
snappy.forward(400)
snappy.setheading(180)
snappy.forward(130)
snappy.setheading(0)


for dot_count in range(1,number_of_dots + 1):
    snappy.dot(20,random.choice(color_list))
    snappy.forward(50)
    if dot_count%10==0:
        snappy.setheading(90)
        snappy.forward(50)
        snappy.setheading(180)
        snappy.forward(500)
        snappy.setheading(0)
        

screen = t.Screen()
screen.exitonclick()

