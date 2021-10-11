from turtle import Turtle
FONT = ('Courier', 11, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

