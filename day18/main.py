from turtle import Turtle
from turtle import Screen
import random

timmy_the_turtle = Turtle()
screen= Screen()
screen.bgcolor('black')
screen.colormode(255)
timmy_the_turtle.shapesize(0.2)
#you can also set rgb color using a tuple inside color() function after activatingg color mode in screen
#we figure out how to use the modules through the documenations
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.pensize(3)
colors = ['red','blue','violet','orange','green','grey','indigo','brown','purple','yellow','dark slate blue','khaki','forest green']
def square():
    for _ in range(3):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)

def draw_line(line_length):
    for _ in range(line_length):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


def draw_shapes(no_of_shapes):
    no_of_sides = 3
    angle = 360/no_of_sides
    for _ in range(no_of_shapes):
        for _ in range(no_of_sides):
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        no_of_sides+=1
        angle= 360/no_of_sides
        timmy_the_turtle.color(select_random_color())

def random_walk(steps):
    possible_ways = [0,1,2,3]
    initial_speed=5
    initial_size=4
    for _ in range(steps):
        initial_size+=0.05
        initial_speed+=0.05
        random_decision = random.choice(possible_ways)
        if random_decision == 0:
            timmy_the_turtle.left(90)
            timmy_the_turtle.forward(20)
        elif random_decision==1:
            timmy_the_turtle.right(90)
            timmy_the_turtle.forward(20)
        elif random_decision==2:
            timmy_the_turtle.forward(20)
        elif random_decision==3:
            timmy_the_turtle.left(180)
            timmy_the_turtle.forward(20)
        timmy_the_turtle.color(random.choice(colors))
        timmy_the_turtle.speed(initial_speed)
        timmy_the_turtle.pensize(initial_size)

directions = [0,90,180,270]
def random_walk_2(steps):
    initial_size=0.1
    for _ in range(steps):
        timmy_the_turtle.color(select_random_color())
        timmy_the_turtle.setheading(random.choice(directions))
        timmy_the_turtle.forward(10)
        timmy_the_turtle.speed("fastest")
        initial_size+=0.02
        timmy_the_turtle.pensize(initial_size)

def select_random_color():
    random_red= random.randint(0,255)
    random_green = random.randint(0,255)
    random_blue = random.randint(0,255)

    return (random_red,random_green,random_blue)
#el random walk sha8ala tmam, fadel ne8ayar el lon, w b3dha nesara3 el turtle el gamela bta3etna

def draw_spirograph(angle_step):
    timmy_the_turtle.speed(10.5)
    for _ in range(int(360/angle_step)):
        timmy_the_turtle.left(angle_step)
        timmy_the_turtle.circle(100)
        timmy_the_turtle.color(select_random_color())

draw_spirograph(0.5)






"""
all the ways you can import a module:
1- import turtle --> import and the module name then you can access the classes through this module
2- from turtle import Turtle --> import the specific class you wanna work with
3- from turtle import * --> this imports all the classes from the module turtle
Note:
-method 3 here actaully is not a professional way as it's really confusing, don't know from where the method come from which module
-avoid trying to write a code like this

__How to alias modules__
import turtle as t --> giving the module as alias name, cause some modules can have a really long name actaully.

Some modules are not installed, you will have to install them through pip on a virtual envinroment
the reason why we have to work with virtual envinroment is actaully a little bit historical problem.
python 2.7 and python 3.12, there is projects on each version, so v.e make you able to choose the version of python you want to run your project on
so we can install the modules based on the compatible versions so we dont cause any problems or errors.
"""
"""
Tuple and what it is:
tuple is similar like a list but its immutable you cant modify it, and its ordered also
and its denoted by rounded parenthesis
my_tuple = (1,3,8)
print(my_tuple[0]) --> 1
my_tuple[0] = 16 --> error, immutable you cannot change it
you can change it by converting it into a list then again to a tuple




"""







screen.exitonclick()
