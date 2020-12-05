from circle import Circle
from typing import Tuple, overload
from turtle import Turtle, color

class GCircle(Circle):
  __op = Turtle()
  __upd = True

  def __init__(self, 
               center: Tuple[float, float], 
               radius: int, 
               op: Turtle = None, 
               clr: color = (0.0, 0.0, 0.0)):
    Circle.__init__(self, center, radius)

    if op != None: self.__op = op
    self.__op.hideturtle()
    self.__op.speed(0)
    self.__op.penup()
    self.__op.setpos((center[0], center[1] - radius))
    self.center = center
    self.__op.color(clr)

    self.radius = radius
  
  def render(self, continuous: bool = True):
    if not continuous and not self.__upd:
      return False

    self.__op.clear()
    self.__op.pendown()
    self.__op.circle(self.radius, steps = 100)
    self.__op.penup()

    self.__upd = False
    return True

  def setCenter(self, center: Tuple[float, float], penup: bool = True):
    if penup: self.__op.penup()
    self.__op.setpos((center[0], center[1] - self.radius))
    if penup: self.__op.pendown()
    self.center = center
    self.__upd = True

  def grow(self, accum = 1):
    Circle.grow(self, accum)
    self.setCenter(self.center)

  def shrink(self, accum = 1):
    Circle.shrink(self, accum)
    self.setCenter(self.center)