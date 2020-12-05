from point import Point
from typing import Tuple, overload
from turtle import Turtle, color

class GPoint(Point):
  __op = Turtle
  __upd = True


  def __init__(self, 
               center: Tuple[float, float],
               radius: int,
               op: Turtle = None, 
               clr: color = (0.0, 0.0, 0.0)):
    Point.__init__(self, center)

    if op != None: self.__op = op
    else: self.__op = Turtle()

    self.__op.hideturtle()
    self.__op.speed(0)
    self.__op.penup()
    self.__op.setpos((center[0], center[1] - radius))
    self.center = center
    self.__op.color(clr, clr)

    self.radius = radius

  
  def changeColor(self, clr: color):
    self.__op.color(clr)
    self.__upd = True


  def render(self, continuous: bool = True):
    if not continuous and not self.__upd:
      return

    self.__op.clear()
    self.__op.begin_fill()
    self.__op.pendown()
    self.__op.circle(self.radius, steps = 4)
    self.__op.penup()
    self.__op.end_fill()

    self.__upd = False

