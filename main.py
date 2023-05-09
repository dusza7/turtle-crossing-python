import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
i = 0
spawn_cars_speed = 10


def gen_car(num):
    global i
    if i % num == 0:
        car_manager.create_car()
    i += 1

screen = Screen()

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    gen_car(spawn_cars_speed)
    car_manager.move()
    scoreboard.update_level()
    for car in car_manager.cars:
        if player.distance(car) < 21:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset()
        car_manager.speed_up()
        if spawn_cars_speed > 1:
            spawn_cars_speed -= 2
    screen.update()

screen.exitonclick()
