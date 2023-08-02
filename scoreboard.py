from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_lvl=1
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.level()

    def level(self):
        self.clear()
        self.write(f"Level:{self.current_lvl}",align="center",font=FONT)

    def increment_lvl(self):
        self.current_lvl+=1
        self.level()