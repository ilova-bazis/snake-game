import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend(snake.segments[-1].position())
        scoreboard.increase_score()

    if snake.head.ycor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290 or snake.head.xcor() > 290:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if segment.distance(snake.head) < 15:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
