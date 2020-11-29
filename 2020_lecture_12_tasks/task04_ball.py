from random import random, randrange

from turtle import Turtle, color
import turtle

from typing import Tuple

class ball:
  def __init__(self,
               scrW: int,
               scrH: int,
               r: int = None, 
               coords: Tuple[float, float] = None,
               speed: float = None,
               dir: Tuple[float, float] = None, 
               op: Turtle = None, 
               clr: color = None):
    self.scrW = scrW
    self.scrH = scrH
               
    if op == None: op = turtle.Turtle()
    self.operator = op
    self.operator.hideturtle()
    self.operator.speed(0)
    self.operator.penup()

    if coords == None: coords = (randrange(-300, 300), randrange(-200, 200))
    self.operator.setpos(coords)

    if speed == None: speed = float(randrange(10, 20) * .00000001)
    self.speed = abs(speed)

    if clr == None: clr = (random(), random(), random())
    self.operator.color("black", clr)

    if dir == None: dir = (float(randrange(-10, 10) * .1), float(randrange(-10, 10) * .1))
    self.direction = dir

    if r == None: r = random() * 20
    self.radius = r

  def update(self, dt: float):
    x = self.operator.pos()[0] + self.direction[0] * self.speed * dt
    y = self.operator.pos()[1] + self.direction[1] * self.speed * dt
    hw = self.scrW / 2
    hh = self.scrH / 2

    self.operator.setpos((x, y))
    
    if (x + self.radius >= hw and self.direction[0] > 0) or (x - self.radius <= -hw and self.direction[0] < 0):
      self.direction = (-self.direction[0], self.direction[1])

    if (y + self.radius >= hh - 18 and self.direction[1] > 0) or (y - self.radius <= -hh and self.direction[1] < 0):
      self.direction = (self.direction[0], -self.direction[1])

  def render(self):
    self.operator.clear()
    self.operator.pendown()
    self.operator.begin_fill()
    self.operator.circle(self.radius, steps = 10)
    self.operator.end_fill()
    self.operator.penup()