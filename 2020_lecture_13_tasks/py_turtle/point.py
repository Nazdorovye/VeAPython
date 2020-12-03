class Point:
  def __init__(self, center: list):
    self.center = center

  def __str__(self) -> str:
    return str(self.center)

  def distance(self, other = None):
    res = ((self.getX() - (0.0 if other == None else other.getX()))**2 + 
           (self.getY() - (0.0 if other == None else other.getY()))**2)**0.5
    return res

  def getX(self):
    return self.center[0]
    
  def getY(self):
    return self.center[1]

  def getCenter(self):
    return self.center

  def move(self, point: list):
    self.center = point