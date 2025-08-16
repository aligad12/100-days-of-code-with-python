from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",24,"normal")


class ScoreBoard(Turtle):
    def __init__(self,snake):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)  # top center for text
        self.score = 0
        self.display_score()
        self.snake = snake

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("Red")
        self.write(arg="GAME OVER",align="center",font=("Courier",35,"bold"))
        
    def game_win(self,snake):
        if len(snake.segments) == 841:
            self.color("gold")
            self.write(arg="You Won!",align="center",font=("Courier",35,"bold"))
            return True
        else:
            return False

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
    
