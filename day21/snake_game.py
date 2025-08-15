from turtle import Screen
import time
from Snake import Snake
from food import Food

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.eat_food(food)



screen.exitonclick()

