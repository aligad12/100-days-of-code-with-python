from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)  # top center for text
        self.score = 0
        self.display_score()  # show initial score

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))


    @staticmethod
    def draw_field():
        line = Turtle()
        line.hideturtle()
        line.penup()
        line.color("white")
        line.goto(-290, -290)  # slightly below scoreboard text
        line.pendown()
        line.forward(580)
        line.left(90)
        line.forward(580)
        line.left(90)
        line.forward(580)
        line.left(90)
        line.forward(580)
