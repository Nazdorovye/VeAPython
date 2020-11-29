
from draw_funcs import drawNgon, drawS, drawSquare, drawV, drawW
import turtle

WND_WIDTH = 640
WND_HEIGHT = 480
REL_SCALE = 0.25



def runTask(ngonSides: int):
  window = turtle.Screen()
  window.setup(WND_WIDTH, WND_HEIGHT, 10, 10)
  window.title("12_Task01")

  trtl = turtle.getturtle()
  trtl.hideturtle()
  trtl.speed(10)

  size = (WND_WIDTH * REL_SCALE if WND_HEIGHT > WND_WIDTH else WND_HEIGHT * REL_SCALE) // 2

  drawSquare((-WND_WIDTH * 0.25, WND_HEIGHT * 0.25), size, trtl, "red")
  drawNgon(ngonSides, (-WND_WIDTH * 0.25, -WND_HEIGHT * 0.25), size, trtl, "black", "cornflower blue")
  drawW((WND_WIDTH * 0.25, WND_HEIGHT * 0.25), 10, size, "blue", trtl)
  drawS((WND_WIDTH * 0.25 - size / 1.5, -WND_HEIGHT * 0.25), 10, size, "orange red", trtl)
  drawV((WND_WIDTH * 0.25 + size / 1.5, -WND_HEIGHT * 0.25), 10, size, "orange red", trtl)

  turtle.Screen().mainloop()