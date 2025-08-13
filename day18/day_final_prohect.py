import colorgram
from turtle import Turtle,Screen
import random

colors = colorgram.extract('hirst_painting_image.jpg',40)
the_colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    the_colors_list.append((r,g,b))

#now we have the list of tuples of the colors we can use the random module to randomly use it
t = Turtle()
s = Screen()
print(t.position())
s.colormode(255)
'''
t.dot(25,random.choice(the_colors_list))
t.penup()
t.forward(50)
t.pendown()
t.dot(25,random.choice(the_colors_list))
t.penup()
#i think we are going now to need a nested loop as we have a repeating sequence each time, but we need to start at the same place again but above
print(t.goto(0,50))
t.dot(25,random.choice(the_colors_list))
t.penup()
t.forward(50)
t.pendown()
t.dot(25,random.choice(the_colors_list))'''
no_of_rows = 10
no_of_cols = 10
initial_y = 0
t.penup()
t.goto(-30,0)
for _ in range(no_of_rows):
    for _ in range(no_of_cols):
        t.dot(25,random.choice(the_colors_list))
        t.penup()
        t.forward(50)
    initial_y+=50
    t.goto(-30,initial_y)



s.exitonclick()



