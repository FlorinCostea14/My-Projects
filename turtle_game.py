import turtle
import random


wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Game")


player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.speed(0)
player.goto(-200, 0)


obstacles = []
for i in range(5):
    obstacle = turtle.Turtle()
    obstacle.color("red")
    obstacle.shape("circle")
    obstacle.penup()
    obstacle.speed(30)
    obstacle.goto(random.randint(-300, 300), random.randint(-200, 200))
    obstacles.append(obstacle)


score = 0
score_pen = turtle.Turtle()
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))


def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)


wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")


while True:
    for obstacle in obstacles:

        obstacle.setx(obstacle.xcor() - 2)


        if player.distance(obstacle) < 20:
            score_pen.clear()
            score_pen.write("Game Over!", align="center", font=("Courier", 24, "normal"))
            wn.update()
            wn.mainloop()

        
        if obstacle.xcor() < -300:
            obstacle.goto(random.randint(300, 500), random.randint(-200, 200))
            score += 1
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    wn.update()
