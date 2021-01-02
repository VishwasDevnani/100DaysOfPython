from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

screen.setup(width = 600, height=600)
user_bet = screen.textinput(title = "Make your bet!!!" ,prompt = "Which turtle will win the race? Enter your choice: ")

colors = ['red','blue','green','yellow','purple']

turtles = []

for index in range (0,5):

    tim = Turtle("turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto( -260,-180 + index*80 )
    turtles.append(tim)


if user_bet:
    is_race_on = True
f = 0
while is_race_on:
    i=-1

    for turtle in turtles:
        i += 1
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                f = 1

        turtle.forward(random.randint(0,10))

if f == 1:
    print(f"Wow!! You won the bet.Winning color is {winning_color}")

    turtles[i].clear()
    turtles[i].goto(-190,0)
    turtles[i].write(f"Wow!! You won the bet.Winning color is {winning_color}", font=("Arial", 16, "normal"))
else:
    print(f"Oopsie!!! You lost the bet.Winning color is {winning_color}")
    turtles[i].clear()
    turtles[i].goto(-190,0)
    turtles[i].write(f"Oopsie!! You lost the bet.Winning color is {winning_color}", font=("Arial", 16, "normal"))

for i in range(5):
    turtles[i].hideturtle()


screen.exitonclick()