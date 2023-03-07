from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Animation Turn Off
screen.tracer(0)

# Creating two objects using same 'Paddle' Class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Creating 'ball' object
ball = Ball()

# Creating 'scoreboard' object
scoreboard = Scoreboard()

# Add Event Listeners
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

# Game On
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_up()

    # Detect Collision With Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to Bounce
        ball.bounce_y()

    # Detect Collision With Left & Right Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect When Right Paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect When Left Paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
