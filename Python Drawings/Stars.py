from turtle import *
from random import *
Screen().bgcolor('black')

def random_color():
  return random(), random(), random()

def star(x, y, side):
    up(), goto(x, y), down(),
    c = random_color()
    pencolor(c), fillcolor(c), begin_fill()
    [(speed(0), rt(144), fd(side)) for _ in range(5)]
    end_fill()

def left_mouse_click(x, y):
  star(x, y, randint(10, 80))

hideturtle(), Screen().onclick(left_mouse_click), Screen().listen()
done()