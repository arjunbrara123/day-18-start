from turtle import Turtle, Screen

import heroes
import random

tim = Turtle()
tim.shape("turtle")
tim.color("magenta2")
cols = ["magenta2", "red", "orange", "green", "blue", "purple"]
random.shuffle(cols)
screen = Screen()
screen.delay(0)
tim.speed("fastest")
# for i in range(36):
#     tim.circle(100)
#     tim.right(10)


def turtle_draw(sides):
    for shape_sides in range(sides):
        tim.forward(100)
        tim.right(360 / float(sides))


screen.colormode(255)
for i in range(500):
    # tCol = str(cols[random.randint(0, 5)])
    # tim.color(tCol)
    side_a = min(255,int(255*abs(tim.pos()[0])/70))
    side_b = min(255,int(255*abs(tim.pos()[1])/70))
    if tim.pos()[0] >= 0:
        side_c = 255-min(255, int((side_a**2 + side_b**2)**0.5))
    else:
        side_c = min(255, int((side_a ** 2 + side_b ** 2) ** 0.5))
    tim.pensize(abs((50-side_c/5)-25))

    tim.pencolor(side_a, side_b, side_c)
    # turtle_draw(int(i))
    rand_dir = random.randint(1, 360)
    tim.right(rand_dir)
    tim.forward(0.5*rand_dir)
    if tim.pos()[0] != 0: tim.setx(tim.pos()[0] * 0.90)
    if tim.pos()[1] != 0: tim.sety(tim.pos()[1] * 0.90)

screen.exitonclick()

print(heroes.gen())
