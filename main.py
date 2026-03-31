from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer()

p1 = Paddle((350,0))
p2 = Paddle((-350,0))
ball = Ball()
score = Scoreboard()


p1_up = False
p1_down = False
p2_up = False
p2_down = False

def p1_up_press():
    global p1_up
    p1_up = True

def p1_up_release():
    global p1_up
    p1_up = False

def p1_down_press():
    global p1_down
    p1_down = True

def p1_down_release():
    global p1_down
    p1_down = False


def p2_up_press():
    global p2_up
    p2_up = True

def p2_up_release():
    global p2_up
    p2_up = False

def p2_down_press():
    global p2_down
    p2_down = True

def p2_down_release():
    global p2_down
    p2_down = False

screen.listen()
# Player 1 (Right paddle)
screen.onkeypress(p1_up_press, "Up")
screen.onkeyrelease(p1_up_release, "Up")
screen.onkeypress(p1_down_press, "Down")
screen.onkeyrelease(p1_down_release, "Down")

# Player 2 (Left paddle)
screen.onkeypress(p2_up_press, "w")
screen.onkeyrelease(p2_up_release, "w")
screen.onkeypress(p2_down_press, "s")
screen.onkeyrelease(p2_down_release, "s")

if p1_up:
    p1.go_up()
if p1_down:
    p1.go_down()

if p2_up:
    p2.go_up()
if p2_down:
    p2.go_down()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(p1) < 50 and ball.xcor() > 320 or \
        ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()