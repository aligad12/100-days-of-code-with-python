from turtle import Screen
from player_turtle import PlayerTurtle
from score_board import ScoreBoard
import time
from Car import Car
from colors import colors
import random

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.setup(600,600)
score_board = ScoreBoard() 
player = PlayerTurtle()
screen.listen()
screen.onkeypress(player.up,"Up")
screen.onkeyrelease(player.stop_moving,"Up")
screen.onkeypress(player.down,"Down")
screen.onkeyrelease(player.stop_moving,"Down")
game_speed = 0.1

game_is_on = True
cars = []

for _ in range(30):
    new_color = random.choice(colors)
    new_car = Car(new_color)
    while any(other.distance(new_car) < 20 for other in cars):
        new_car.reset_position()
    cars.append(new_car)

def check_car_position(cars):
    for car in cars:
        while any(other.distance(car) < 30 for other in cars if other != car):
            car.reset_position()

def increase_game_speed(game_speed):
    return game_speed*0.99

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    player.move()
    
    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset_position()
            check_car_position(cars)
        if car.distance(player) < 20:
            game_is_on = False
            score_board.lose()
        if score_board.game_level == 20:
            score_board.win()
            break
    
    if player.ycor() >= 255 :
        player.reset_position()
        score_board.update_level()
        for car in cars:
            car.reset_position()
            check_car_position(cars)
            game_speed = increase_game_speed(game_speed)


    




screen.exitonclick()