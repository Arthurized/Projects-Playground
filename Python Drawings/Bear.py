import turtle as t
t.speed(0), t.hideturtle()


def krug(k):
  b = 0
  while k > 0:
    t.circle(k)
    k -= 1
    b += 1
    if b == 3: t.pensize(8)
  t.pencolor('black'), t.pensize(1)


t.up(), t.goto(0, -40), t.down(), t.pencolor('darkorange'), krug(90), t.pencolor('goldenrod'), krug(50)
a = t.pos()
t.up(), t.goto(60, 122), t.down(), t.pencolor('lightsalmon'), krug(30), t.up(), t.goto(-60, 122), t.down()
t.pencolor('lightsalmon'), krug(30), t.up(), t.goto(a[0], a[1] + 25), t.down(), t.setheading(90), t.fd(40)
t.setheading(0), t.pencolor('lemonchiffon'), krug(9)
b = t.pos()
t.up(), t.goto(b[0] + 42, b[1] + 38), t.down(), t.dot(18), t.goto(b[0] + 40, b[1] + 37), t.pencolor('white')
t.dot(5), t.pencolor('black'), t.up(), t.goto(b[0] - 42, b[1] + 38), t.down()
t.dot(18), t.goto(b[0] - 40, b[1] + 37), t.pencolor('white'), t.dot(5)
t.done()
