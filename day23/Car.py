from turtle import Turtle
import random 

class Car(Turtle):
    def __init__(self,color):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        y_value = random.randint(-300,240)
        x_value = random.randint(300,600)
        self.shapesize(stretch_len=1.2,stretch_wid=0.8)
        self.goto(x_value,y_value)

    def move(self):
        self.setheading(180)
        self.forward(10)

    def reset_position(self):
        new_y = random.randint(-300,240)
        new_x = random.randint(300,600)
        self.goto(new_x,new_y)

    