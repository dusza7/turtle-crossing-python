from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(90)
        new_car.shape("square")
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.level), car.ycor())

    def speed_up(self):
        self.level += 1

