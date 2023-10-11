from turtle import Screen
from ball import Ball
import time
from paddels import Paddel
from score import Score


screen = Screen()
screen.title("pong")
ball = Ball()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800, height=600)


r_paddel = Paddel()
l_paddel = Paddel()
r_paddel.paddle(350, 0)
l_paddel.paddle(-350, 0)

score=Score()
score.score()


screen.listen()
screen.onkey(r_paddel.up, "w")
screen.onkey(r_paddel.down, "s")
screen.onkey(l_paddel.up, "Up")
screen.onkey(l_paddel.down, "Down")


game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()

    if(ball.distance(r_paddel) < 50 and ball.xcor() > 320):
        ball.bounces()

    if ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounces()

    if ball.xcor() > 380:
        ball.reset()
        score.lpoint()

    if ball.xcor() < -380:
        ball.reset()
        score.rpoint()











screen.exitonclick()