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

def check_screen_collisions():
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        return True


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.eat_food(food)
    if snake.check_collision_with_tail() == True:
        print("You lost!")
        game_is_on = False
    if check_screen_collisions() == True:
        print("You lost!")
        game_is_on = False



screen.exitonclick()

