from turtle import Screen, Turtle

screen = Screen()

# Setup screen
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
