from draw_funcs import star
import turtle

WND_WIDTH = 640
WND_HEIGHT = 480
REL_SCALE = 0.5
  


def runTask(starSides: int):
  window = turtle.Screen()
  window.setup(WND_WIDTH, WND_HEIGHT, 10, 10)
  window.title("12_Task02")

  trtl = turtle.getturtle()
  trtl.hideturtle()
  trtl.speed(10)

  size = WND_WIDTH * REL_SCALE if WND_HEIGHT > WND_WIDTH else WND_HEIGHT * REL_SCALE

  star(starSides, size, trtl)

  turtle.Screen().mainloop()