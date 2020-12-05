from task05_gcircle import GCircle
from task05_wnd import Wnd

from typing import Tuple

SCROLL_MAGN = 4

def mouse_wheel(event):
    # Linux && Windows events
    if event.num == 5 or event.delta == -120:
        circ.grow(SCROLL_MAGN)
    if event.num == 4 or event.delta == 120:
        circ.shrink(SCROLL_MAGN)

wnd = Wnd("13_Task05", 640, 480, 10, 10)
wnd.setOnMouseClick(lambda x, y: circ.setCenter((x, y)))
wnd.setOnMouseWheel(mouse_wheel)

circ = GCircle((0, 0), 220)

while wnd.getRunning():
  circ.render(False)
  wnd.update()