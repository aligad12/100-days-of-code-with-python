from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,screen,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize()
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.color("white")
        self.goto(position,0)
        self.moving_up = False
        self.moving_down = False
        self.screen = screen

        
    def detect_collision(self,ball):
        pass

    def up_pressed(self):
        self.setheading(90)
        self.moving_up = True

    def up_released(self):
        self.moving_up = False

    def down_pressed(self):
        self.setheading(270)
        self.moving_down = True

    def down_released(self):
        self.moving_down = False

    def move_while_pressed(self):
        if self.moving_up and self.ycor() < 220:   
            self.goto(self.xcor(), self.ycor() + 20)
        if self.moving_down and self.ycor() > -250:  
            self.goto(self.xcor(), self.ycor() - 20)