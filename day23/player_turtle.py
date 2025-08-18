from turtle import Turtle

class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        self.move_up = False
        self.move_down = False



    def up(self):
        self.setheading(90)
        self.move_up = True
    
    def down(self):
        self.setheading(270)
        self.move_down = True

    def stop_moving(self):
        self.move_up = False
        self.move_down = False

    def move(self):
        if self.move_up:
            new_y = self.ycor() +10
            new_x = self.xcor()
            self.goto(new_x,new_y)
        elif self.move_down:
            new_y = self.ycor() -10
            new_x = self.xcor()
            self.goto(new_x,new_y)


    def reset_position(self):
        self.goto(0,-290)
        