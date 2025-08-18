from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.game_level = 0
        self.display_level()


    def display_level(self):
        self.clear()
        self.goto(0,260)
        self.write(arg=f"Level: {self.game_level}",align="center",font=("Courier",25,"normal"))
        self.draw_horizontal_line()

    def draw_horizontal_line(self):
        self.goto(-310, 245)
        self.pendown()
        self.forward(630)
        self.penup()

    def update_level(self):
        self.game_level+=1
        self.display_level()

    def win(self):
        self.color("yellow")
        self.goto(0,0)
        self.write(arg=f"You Won!",align="center",font=("Courier",24,"bold"))

    def lose(self):
        self.color("red")
        self.goto(0,0)
        self.write(arg=f"Game Over.",align="center",font=("Courier",24,"bold"))
