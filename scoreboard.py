from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.color("white")
        self.goto(-230, 260)
        self.pendown()
        self.update_level()
        self.ht()

    def update_level(self):
        self.write(f"LEVEL: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()


