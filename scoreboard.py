from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"), align="center")

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)

        self.write("GAME OVER",  font=("Arial", 24, "normal"), align="center")