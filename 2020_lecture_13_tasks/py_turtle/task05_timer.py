import time

class timer:
  __interval: int
  __ticker = 0
  __passed = False

  # === MAGIC METHODS ==============================================================================
  def __init__(self, ns_interval: int):
    self.setInterval(ns_interval)

  # === OPERATIONAL METHODS ========================================================================
  def tick(self, dt: int):
    self.__ticker += dt

    if (self.__ticker >= self.__interval):
      self.__passed = True
      self.__ticker = 0
  
  # === GET/SET METHODS ============================================================================
  def peekInterval(self) -> int:
    return self.__interval

  def setInterval(self, ns_interval: int):
    if ns_interval < 0:
      print("Invalid interval (%d), taking abs(%d)" % (ns_interval, ns_interval))
      ns_interval = abs(ns_interval)
    self.__interval = ns_interval

  def peekTicker(self) -> int:
    return self.__ticker

  def peekPassed(self) -> bool:
    return self.__passed

  def setPassed(self):
    self.__passed = False



class timerMgr:
  __t0 = time.time_ns()
  __dt = 0
  __trs = []
  
  # === OPERATIONAL METHODS ========================================================================
  def tick(self):
    t1 = time.time_ns()
    self.__dt = t1 - self.__t0
    self.__t0 = t1

    for tmr in self.__trs:
      tmr.tick(self.__dt)

  def addTimer(self, ns_interval: int = 1000000000) -> timer:
    self.__trs.append(timer(ns_interval))
    return self.__trs.__getitem__(len(self.__trs) - 1)

  # === GET/SET METHODS ============================================================================
  def peekDt(self) -> int:
    return self.__dt