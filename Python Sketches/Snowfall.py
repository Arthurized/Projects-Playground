import turtle as t
from random import randint, choice
t.hideturtle(), t.speed(0), t.pensize(3)

height, length = (int(input('Please, enter the height of the window, 500 recommended: ')),
                  int(input('Please, enter the length of the window, 500 recommended: ')))
t.Screen().setup(height, length), t.Screen().bgcolor('cyan')
colours = ['Green', 'navy', 'snow', 'wheat', 'SteelBlue', 'LightGoldenrod', 'DarkSlateGray', 'DodgerBlue', 'DarkOrchid',
           'ivory']
xcor = [i for i in range(-(height//2) + 60, height//2 - 60, 85)]
ycor = [i for i in range(-(length//2) + 60, length//2 - 60, 85)]
b = 0


def bok():
    for _ in range(3):
        t.fd(k*3/2)
        post = t.pos()
        t.lt(60), t.fd(k), t.up(), t.goto(post[0], post[1]), t.down(), t.rt(120), t.fd(k), t.up(),
        t.goto(post[0], post[1]), t.lt(60), t.down()


def snowflake(x_, y_):
    t.up(), t.goto(x_, y_), t.down()
    position = t.pos()
    t.pencolor(choice(colours))
    [(t.dot(6), bok(), t.fd(k*3/2), t.up(), t.goto(position[0], position[1]), t.down(), t.lt(45)) for _ in range(8)]


for _ in range(len(xcor)):
    k = randint(4, 15)
    while k*4 + b*4 > 80:
        k = randint(4, 15)
    b = k
    x, y = choice(ycor), choice(xcor)
    snowflake(x, y)
    xcor.remove(y), ycor.remove(x)
t.pencolor('Red'), t.up(), t.setheading(0), t.fd(100), t.down(),
t.write('Happy New Year!🎭', align='left', font=('Times New Roman', 25, 'italic')), t.exitonclick()