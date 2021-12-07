from turtle import Turtle
FONT = ('Courier', 11, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
