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
paddle_1 = Paddle(screen,-350)
paddle_2 = Paddle(screen,350)
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
    time.sleep(ball.ball_speed)
    paddle_1.move_while_pressed()
    paddle_2.move_while_pressed()
    ball.move()
    if ball.ycor() > 250 or ball.ycor() < -270:
        ball.bounce_y()
    
    elif ball.xcor() > 330 and paddle_2.ycor() - 50 < ball.ycor() < paddle_2.ycor() + 50:
        ball.bounce_x()
        ball.increase_ball_speed()

    elif ball.xcor() < -330 and paddle_1.ycor() - 50 < ball.ycor() < paddle_1.ycor() + 50:
        ball.bounce_x()
        ball.increase_ball_speed()     
    
    elif ball.xcor() > 350:
        ball.reset_position()
        score.update_score_left()

    elif ball.xcor() < -350:
        ball.reset_position()
        score.update_score_right()

       










screen.exitonclick()