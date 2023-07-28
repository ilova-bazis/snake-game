from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # 20 * 0.5 = 10
        self.refresh()



    def refresh(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x, y)