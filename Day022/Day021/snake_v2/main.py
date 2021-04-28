from turtle import Turtle,Screen
import time
from snake_v2 import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()


screen.title("Snake Game")
snake = Snake()
food = Food()
 

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    for i in range(1,len(snake.segment)):
        if snake.head.distance(snake.segment[i]) < 10:
            scoreboard.game_over()
            game_is_on = False

    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()