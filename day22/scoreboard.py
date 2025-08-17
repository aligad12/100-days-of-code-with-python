from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left= 0
        self.score_right=0
        self.display_score() #this line to display the initial score
    
    def display_score(self):
        self.clear()
        self.goto(0,280)
        self.write(arg=f"{self.score_left} | {self.score_right}",align="center",font=("Courier",25,"normal"))


    def draw_boarder():
        new = Turtle()
        new.color("white")
        new.hideturtle()
        new.penup()
        new.goto(0,-325)
        new.setheading(90)
        for _ in range(30):
            new.pendown()
            new.forward(10)
            new.penup()
            new.forward(10)
        new.penup()
        new.goto(-400,270)
        new.pendown()
        new.setheading(0)
        new.forward(800)

    def update_score_left(self):
        self.score_left+=1
        self.display_score()

    def update_score_right(self):
        self.score_right+=1
        self.display_score()

