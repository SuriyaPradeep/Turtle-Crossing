import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

tur = Turtle()
tur.hideturtle()
tur.color("red")
tur.goto(0,0)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
    if player.check_finish():
        player.goto_start()
        car_manager.increase_speed()
        scoreboard.increment_lvl()


tur.write("GAME OVER", align="center", font=("Arial", 20, "bold"))

screen.exitonclick()
