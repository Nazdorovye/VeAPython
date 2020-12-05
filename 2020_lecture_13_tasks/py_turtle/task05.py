from task05_gcircle import GCircle
from task05_gpoint import GPoint
from task05_timer import *
from task05_wnd import Wnd

from random import randrange

SCROLL_MAGN = 4
POINT_CNT = 50
WND_W = 640
WND_H = 480

def mouse_wheel(event):
    # Linux && Windows events
    if event.num == 5 or event.delta == -120:
        circ.grow(SCROLL_MAGN)
    if event.num == 4 or event.delta == 120:
        circ.shrink(SCROLL_MAGN)

wnd = Wnd("13_Task05", 640, 480, 10, 10)
wnd.setOnMouseClick(lambda x, y: circ.setCenter((x, y)))
wnd.setOnMouseWheel(mouse_wheel)

hw = WND_W // 2
hh = WND_H // 2

circ = GCircle((0, 0), 220)
points = [GPoint((randrange(-hw, hw), randrange(-hh, hh)), 2, clr="RED") for _ in range(POINT_CNT)]

tMgr = timerMgr()
fpsTimer = tMgr.addTimer(33333333)
tpsTimer = tMgr.addTimer(8333333)
redrawPoints = True

while wnd.getRunning():
  tMgr.tick()

  if tpsTimer.peekPassed():
    tpsTimer.setPassed()

    if redrawPoints:
      for point in points:
        if point.distance(circ) <= circ.getRadius():
          point.changeColor("BLUE")
        else:
          point.changeColor("RED")

      redrawPoints = False

  if fpsTimer.peekPassed():
    fpsTimer.setPassed()

    redrawPoints = circ.render(False)
    for p in points:
      p.render(False)

  wnd.update()
