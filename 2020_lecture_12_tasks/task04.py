from task04_timer import timerMgr
from task04_ball import ball

import turtle

def stop():
  global running
  running = False

WND_WIDTH = 640
WND_HEIGHT = 480

running = True

window = turtle.Screen()
window.setup(WND_WIDTH, WND_HEIGHT, 10, 10)
window.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", stop) # catch X button
window.title("12_Task04")
window.delay(0)

balls = [ball(WND_WIDTH, WND_HEIGHT) for _ in range(10)]

# TIMERS
tMgr = timerMgr()
secTimer = tMgr.addTimer()
frmTimer = tMgr.addTimer(33333333) # 30 fps == 1000000000 ns / 30 frames
tps = 0
fps = 0

# MAIN
while running:
  tMgr.tick()
  tps += 1

  for b in balls:
    b.update(tMgr.peekDt())

  if frmTimer.peekPassed():
    frmTimer.setPassed()
    fps += 1
    for b in balls:
      b.render()      

  if secTimer.peekPassed():
    secTimer.setPassed()
    window.title(str.format("12_Task04 : TPS:%d FPS:%d" % (tps, fps)))
    tps = 0
    fps = 0

  window.update()