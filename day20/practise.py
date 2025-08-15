"""
we first need to break our problem into a small goals
1- create a snake body
2- move the snake
3- control the snake using keyboard controls
4-detect collision with food
5-create a scoreboard
6-detect collision with wall --> to detect when game ends
7- detect collision with tail --> to detect when game ends aswell
"""
from turtle import Screen,Turtle

def draw_rectangle(snake):
    snake.speed(50)
    snake.begin_fill()
    snake.forward(20)
    snake.left(90)
    snake.forward(10)
    snake.left(90)
    snake.forward(20)
    snake.left(90)
    snake.forward(10)
    snake.end_fill()



screen = Screen()
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("Black")
snake = Turtle()
def move_right():
    if snake.heading() != 180:
        snake.setheading(0)
        screen.clear()
        screen.bgcolor("Black")
        snake.penup()
        snake.forward(50)
        snake.pendown()
        draw_rectangle(snake)

def move_up():
    screen.clear()
    screen.bgcolor("Black")
    if snake.heading() != 270:
        snake.setheading(90)
        snake.penup()
        snake.forward(50)
        snake.pendown()
        draw_rectangle(snake)

def move_left():
    screen.clear()
    screen.bgcolor("Black")
    if snake.heading() != 0:
        snake.setheading(180)
        snake.penup()
        snake.forward(50)
        snake.pendown()
        draw_rectangle(snake)

def move_down():
    if snake.heading() != 90:
        snake.setheading(270)
        screen.clear()
        screen.bgcolor("Black")
        snake.penup()
        snake.forward(50)
        snake.pendown()
        draw_rectangle(snake)

screen.listen()
screen.onkey(key="Right",fun=move_right)
screen.onkey(key="Left",fun=move_left)
screen.onkey(key="Up",fun=move_up)
screen.onkey(key="Down",fun=move_down)

snake.color("green")
snake.shapesize(0.1)
snake.pencolor("green")
draw_rectangle(snake)
#how are we going to create a snake body now
#so to simulate a motion actaully we need to delete the previous canvas and draw a new one to make it seem like its moving, el khatwa el wahda hatb2a b hagm el object

screen.exitonclick()