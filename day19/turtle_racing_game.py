from turtle import Turtle,Screen
import random

#making the turtle race game, first im gonna set the window right size
screen = Screen()
screen.setup(width=500,height=400) #here recommend using keyword argument rather than positional argument so its easier to understand
colors = ['red','green','blue','violet','black','indigo','orange','brown']

def create_turtle_objects(num_of_turtles):
    turtles = []
    used_colors=[]
    y_position = -50
    for _ in range(num_of_turtles):
        new_turtle = Turtle(shape="turtle")
        while True:
            new_color = random.choice(colors)
            if new_color not in used_colors:
                new_turtle.color(new_color)
                used_colors.append(new_color)
                new_turtle.penup()
                new_turtle.goto(-220,y_position)
                break
            else:
                continue
        y_position+=30
        turtles.append(new_turtle)
    return turtles


turtles = create_turtle_objects(6)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            print(f"The {turtle.pencolor()} Won the race!")
            if user_bet == turtle.pencolor():
                is_race_on = False
                print("You Won!")
                break
            else:
                is_race_on = False
                print("You Lost!")
                break



screen.exitonclick()
