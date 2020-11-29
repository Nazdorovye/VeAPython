import math
from turtle import Turtle, color

def moveTo(pos: tuple, op: Turtle):
  op.penup()
  op.setpos(pos)
  op.pendown()



def drawNgon(n: int, pos: tuple, size: float, op: Turtle, border: color, fill: color = None):
  radius = size / (0.25 * n * math.sin(math.pi / n))

  moveTo((pos[0], pos[1] - radius), op)
  if fill == None:
    op.color(border) 
    op.circle(radius, steps=n)
  else:
    op.color(border, fill)
    op.begin_fill()
    op.circle(radius, steps=n)
    op.end_fill()



def drawSquare(pos: tuple, size: float, op: Turtle, fill: color = None):
  indices = [ (pos[0] - size, pos[1] + size),
              (pos[0] + size, pos[1] + size),
              (pos[0] + size, pos[1] - size),
              (pos[0] - size, pos[1] - size),
            ]

  moveTo(indices[3], op)
  op.color("black") if fill == None else op.color("black", fill)
  op.begin_fill()

  for i in range(0, len(indices)):
    op.setpos(indices[i])
  
  op.end_fill()



def drawS(pos: tuple, thickness: int, size: float, color: color, op: Turtle):
  op.color(color)
  op.pensize(thickness)

  moveTo((pos[0] + size / 2, pos[1] + size), op)
  op.setpos(pos[0], pos[1] + size)
  op.circle(-size / 2, -180, 8)
  op.circle(size / 2, -180, 8)
  op.setpos(pos[0] - size / 2, pos[1] - size)



def drawV(pos: tuple, thickness: int, size: float, color: color, op: Turtle):
  op.color(color)
  op.pensize(thickness)

  moveTo((pos[0] - size / 2, pos[1] + size), op)
  op.setpos(pos[0], pos[1] - size)
  op.setpos(pos[0] + size / 2, pos[1] + size)



def drawW(pos: tuple, thickness: int, size: float, color: color, op: Turtle):
  op.color(color)
  op.pensize(thickness)

  moveTo((pos[0] - size / 0.75, pos[1] + size), op)
  op.setpos(pos[0] - size / 1.5, pos[1] - size)
  op.setpos(pos[0], pos[1] - size / 3)
  op.setpos(pos[0] + size / 1.5, pos[1] - size)
  op.setpos(pos[0] + size / 0.75, pos[1] + size)



def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  
  return a



def star(n: int, size: float, op: Turtle):
  if n < 5:
    return

  for cpr in range(n // 2, 1, -1):
    if gcd(n, cpr) == 1:
      angle = 360. / n * cpr

      moveTo((op.pos()[0] - size / 2, op.pos()[1] + 
        size / 2 * math.cos(angle / 2) * math.sin(angle / 2)), op)

      start = op.pos()

      for _ in range(n):
        op.forward(size)
        op.left(angle)

      op.setpos(start)
      return

  # 6-pointed star exception
  for _ in range(3):
    op.forward(size)
    op.right(120)

  op.penup()
  op.right(120)
  for i in range(2):
    op.forward(size / 3)
    op.left(60)
  op.pendown()

  for x in range(3):
    op.forward(size)
    op.left(120)