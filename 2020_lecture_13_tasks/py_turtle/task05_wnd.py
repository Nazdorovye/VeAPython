from turtle import Screen, onclick
from typing import Any, Callable

class Wnd:
  __wnd = Screen()
  __resizeable: bool
  __running: bool

  def __init__(self, title: str, w: int, h: int, x: int, y: int, resizeable: bool = False):
    self.__resizeable = resizeable
    self.__wnd.setup(w, h, x, y)
    self.__wnd.title(title)
    self.__wnd.delay(0)
    self.__wnd.cv._rootwindow.resizable(resizeable, resizeable)
    # catch X button
    self.__wnd.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.stop) 
    self.__running = True

    self.__wnd.listen()

  def update(self): self.__wnd.update()
  def stop(self): self.__running = False
  def getRunning(self): return self.__running
  def setOnMouseClick(self, fun: Callable[[float, float], Any]): self.__wnd.onclick(fun)

  def setOnMouseWheel(self, fun: Callable[[float], Any]):
    # Windows pfm
    self.__wnd.cv.bind("<MouseWheel>", fun)
    # Linux pfm
    self.__wnd.cv.bind("<Button-4>", fun)
    self.__wnd.cv.bind("<Button-5>", fun)

  def setTitle(self, title: str):
    self.__wnd.title(title)