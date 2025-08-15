from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #here we stretched it to have its size
        self.color("blue")
        self.speed("fastest")
        random_x= random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
# i think we need to avoid generating the food at a position of the snake segments also to be able to make the win condition

    def refresh_food(self,snake):
        while True:
            random_x= random.randint(-280,280)
            random_y = random.randint(-280,280)
            if all(segment.distance(random_x,random_y) >=20 for segment in snake.segments):
                self.goto(random_x,random_y)
                break
            