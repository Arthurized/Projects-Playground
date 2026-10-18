from turtle import *
from random import *
Screen().setup(400, 300), Screen().bgcolor('MidnightBlue'), speed(0), hideturtle()
sp = []
[(up(), goto(randint(-200, 200), randint(-100, 150)), down(), pencolor(choice(['white', 'lightcyan', 'coral', 'gold', 'lightsalmon'])), dot(uniform(2.5, 2.9))) for _ in range(90)]
up(), goto(-200, -150), setheading(90), down(), pencolor('royalblue')

def building(side):
  fillcolor('royalblue'), begin_fill()
  [(pencolor('black'), fd(side), rt(90), fd(side/5), rt(90), pencolor('royalblue')) for _ in range(2)]
  setheading(0), fd(side/5), setheading(90), end_fill()

def window():
  pencolor('yellow'), fillcolor('yellow')
  [(begin_fill(), fd(2), rt(90)) for _ in range(4)]
  end_fill()

for _ in range(1000):
  side = randrange(20, 145, 5)
  if side not in sp:
    building(side)
    sp.append(side)
    x = xcor()
    y = ycor()
    if side > 25:
      [(up(), goto(randint(int(x) - (side//5) + 2, int(x) - 4), randint(-150, - 150 + side - 10)), down(), window()) for _ in range((side + 50)//50)]
      pencolor('royalblue'), up(), goto(x, y), down()

up(), goto(0, 50), down()
fillcolor('#53BAAF'), pencolor('#53BAAF')
write('💥Welcome to our city!💥', align='center', font=('Times New Roman', 24, 'normal', 'bold'))
done()
