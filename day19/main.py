import random
from turtle import Turtle,Screen

t = Turtle()
s = Screen()

def pen_down():
    t.pendown()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    new_heading= t.heading()+10
    t.setheading(new_heading)

def turn_right():
    new_heading= t.heading()-10
    t.setheading(new_heading)


def pen_up():
    t.penup()

def clear():
    t.clear()
    t.penup()
    t.home()


s.listen()
s.onkey(key="Right",fun=turn_right)
s.onkey(key="Up",fun=move_forward)
s.onkey(key="Down",fun=move_backward)
s.onkey(key="Left",fun=turn_left)
s.onkey(key="space",fun=pen_down)
s.onkey(key="u",fun=pen_up)
s.onkey(key="Escape",fun=clear)

"""
to be able to use keys in turtle module and modules you actaully need an event listener
thats why we used s.listen()
which enables the program to connect to the keyboard hardware and listen
and then we connect each function to a specific key through the onkey method here as we write the name of the key and give it the name of the function
just passing the function name so the onkey method can activate it whenever it listens to a key press, we do not put parenthesis
as if we do we are triggering the method


"""
s.exitonclick()