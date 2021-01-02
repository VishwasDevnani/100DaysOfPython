from turtle import Turtle,Screen

snappy = Turtle()
screen = Screen()

def move_forward():
    snappy.forward(10)

def move_backard():
    snappy.backward(10)

def turn_left():
    snappy.setheading( snappy.heading() + 10 )

def turn_right():
    snappy.setheading( snappy.heading() - 10 )

def clear():
    snappy.clear()
    snappy.home()

screen.listen()
screen.onkey(move_forward , " w ")
screen.onkey(move_backard , " s ")
screen.onkey(turn_left , " a ")
screen.onkey(turn_right , " d ")
screen.onkey(clear , " c ")

screen.exitonclick()