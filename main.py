from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()

# Setup screen
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(position=(-350, 0))
r_paddle = Paddle(position=(350, 0))
ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    sleep(0.08)
    screen.update()
    ball.move()

screen.exitonclick()
