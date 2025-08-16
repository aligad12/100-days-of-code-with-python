from turtle import Screen
import time
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800,height=650)
screen.title("The Famous Pong Game")
screen.listen()
ball = Ball()
paddle_1 = Paddle(screen)
paddle_1.move_paddle(-350)
paddle_2 = Paddle(screen)
paddle_2.move_paddle(350)
score = ScoreBoard()
score.display_score()
ScoreBoard.draw_boarder()
game_is_on = True

screen.onkeypress(key="Up",fun=paddle_1.up_pressed)
screen.onkeyrelease(key="Up",fun=paddle_1.up_released)
screen.onkeypress(key="Down",fun=paddle_1.down_pressed)
screen.onkeyrelease(key="Down",fun=paddle_1.down_released)
screen.onkeypress(key="w",fun=paddle_2.up_pressed)
screen.onkeyrelease(key="w",fun=paddle_2.up_released)
screen.onkeypress(key="s",fun=paddle_2.down_pressed)
screen.onkeyrelease(key="s",fun=paddle_2.down_released)

while game_is_on:
    screen.update()
    time.sleep(0.05)
    paddle_1.move_while_pressed()
    paddle_2.move_while_pressed()










screen.exitonclick()