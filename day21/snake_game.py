from turtle import Screen,Turtle
import time
from Snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(width=650,height=670,startx=400, starty=-0.4)
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
score_board = ScoreBoard()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

def check_screen_collisions():
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        print(snake.head.position())
        return True
def game_over():
    game_over = Turtle()
    game_over.color("Red")
    game_over.write(arg="GAME OVER",align="center",font=("Courier",35,"bold"))

def game_win():
    if len(snake.segments) == 841:
        return True
    else:
        return False

game_is_on = True
ScoreBoard.draw_field()
game_speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()
    if snake.eat_food(food):
        score_board.update_score()
        game_speed-=0.001
    if snake.check_collision_with_tail() == True:
        print("You lost!")
        game_is_on = False
        game_over()
    if check_screen_collisions() == True:
        print("You lost!")
        game_is_on = False
        game_over()
    if game_win():
        winner = Turtle()
        winner.color("gold")
        winner.write(arg="You Won!",align="center",font=("Courier",35,"bold"))



screen.exitonclick()

