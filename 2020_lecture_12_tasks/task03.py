from turtle import color
from draw_funcs import drawNgon, star
import turtle
import random

WND_WIDTH = 640
WND_HEIGHT = 480
REL_SCALE = 0.9
  


def runTask(n: int, k: int):
  window = turtle.Screen()
  window.setup(WND_WIDTH, WND_HEIGHT, 10, 10)
  window.title("12_Task03")

  trtl = turtle.getturtle()
  trtl.hideturtle()
  trtl.speed(10)

  size = (WND_WIDTH * REL_SCALE if WND_HEIGHT > WND_WIDTH else WND_HEIGHT * REL_SCALE) // 2.5

  trtl.pensize(5)
  for i in range(k):
    r = random.random()
    g = random.random()
    b = random.random()
    drawNgon(n, (0, 0), size, trtl, (r, g, b))
    size -= 5

  turtle.Screen().mainloop()