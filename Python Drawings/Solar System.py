from turtle import *
from math import *
from random import *


def ellipse(a, b, angle):
    pencolor(215, 255, 254)
    cx = xcor()
    cy = ycor()
    turn = 0
    x = cx + a * cos(turn) * cos(radians(angle)) - b * sin(turn) * sin(radians(angle))
    y = cy + a * cos(turn) * sin(radians(angle)) + b * sin(turn) * cos(radians(angle))
    up()
    goto(x, y)
    down()
    n = 2100
    for z in range(n):
        tracer(10, 0)
        x = cx + a * cos(turn) * cos(radians(angle)) - b * sin(turn) * sin(radians(angle))
        y = cy + a * cos(turn) * sin(radians(angle)) + b * sin(turn) * cos(radians(angle))
        if 320 < z < 670:
            up()
        else:
            down()
        goto(x, y)
        turn += 2 * pi / n


Screen().bgcolor('black'), colormode(255)
speed(0), hideturtle()
[(up(), goto(randint(-200, 200), randint(-200, 200)), down(), pencolor('white'), dot(2.5) )for _ in range(100)]
pencolor('grey'), pensize(0.5)

k = 4.5
diameters = [109.245, 0.383, 0.950, 1, 0.532, 10.973, 9.14, 3.981, 3.865, 0.181]
r = (255, 202, 202, 1, 161, 197, 234, 144, 46, 152)
g = (204, 185, 165, 126, 37, 112, 214, 227, 93, 118)
b = (51, 186, 180, 126, 27, 82, 184, 255, 157, 84)
up(), goto(-170, 0), setheading(90), down()

for i in range(10):
    if i == 9:
      pensize(2.2)
    setheading(90), fillcolor(r[i], g[i], b[i]), begin_fill(),
    circle(diameters[i] * k), end_fill(), setheading(0)
    if i == 6:
      sp = pos()
      [(up(), goto(sp[0] - 40, sp[1] - 5), down(), ellipse(60 + 3*l, 30, 45)) for l in range(8)]
      pencolor('grey'), up(), goto(sp[0], sp[1]), down()
    if i <= 8:
        up(), fd(diameters[i + 1]*k*2 + 10), down()

names = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
fillcolor('white')
up(), goto(-170, 180), write(names[0], move=False, align='center', font=('TimesNewRoman', 12, 'bold'))
[(up(), goto(-146 + (j - 1) * 45, -90) if j == 2 else goto(-146 + (j - 1) * 40, -90), write(names[j], move=False, align='center', font=('TimesNewRoman', 7, 'bold'))) for j in range(1, 10)]
done()