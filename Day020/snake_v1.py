from turtle import Turtle,Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class new_turtle:
    def __init__(self, x = 0, y = 0):
        self.segments = []
        self.snappy = Turtle("square")
        self.snappy.penup()
        self.snappy.color("white")
        self.snappy.goto(x , y)
    def move_forward(self):
        self.snappy.forward(20)
    def turn_left(self):
        if self.head() != RIGHT:
            self.snappy.setheading( LEFT )
    def turn_right(self):
        if self.head() != LEFT:
            self.snappy.setheading( RIGHT )
    def up(self):
        if self.head() != DOWN:
            self.snappy.setheading( UP )
    def down(self):
        if self.head() != UP:
            print("Down")
            self.snappy.setheading( DOWN )
    def xy(self):
        return self.snappy.xcor() , self.snappy.ycor()
    def follow(self,a,b):
        self.snappy.goto(a,b)
    def move(self):
        self.snappy.backward(5)
    def head(self):
        self.snappy.heading()


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Nokia3310")
screen.tracer(0)

segments = []
for i in range(3):
    segments.append( new_turtle( x = i*(-20) ) )



game_is_on = True
screen.listen()
while game_is_on:
    screen.listen()
    screen.update()
    
    time.sleep(0.5)
    for i in range(len(segments)-1,0,-1):
        new_x,new_y = segments[i-1].xy()
        segments[i].follow(new_x, new_y)

    #if segments[0].head() != DOWN:
    screen.onkey(segments[0].up,"w")
    #if segments[0].head() != UP:
    screen.onkey(segments[0].down,"s")
    #if segments[0].head() != RIGHT:
    screen.onkey(segments[0].turn_left,"a")
    #if segments[0].head() != LEFT:
    screen.onkey(segments[0].turn_right,"d")
    segments[0].move_forward()      


screen.exitonclick()