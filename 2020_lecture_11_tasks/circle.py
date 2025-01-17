class Circle:
  def __init__(self, center: list, radius: int):
    self.center = center
    self.radius = abs(radius)

  def __str__(self) -> str:
    return str.format("<%s, %d>" % (self.center, self.radius))

  def distance(self, other = None):
    return ((self.getX() - 0.0 if other == None else other.getX())**2 + 
            (self.getY() - 0.0 if other == None else other.getY())**2)**0.5

  def move(self, point):
    self.center = point

  def grow(self): 
    self.radius += 1

  def shrink(self):
    if self.radius > 0:
      self.radius -= 1

  def getArea(self):
    from math import pi
    return pi * self.radius ** 2

  def getCircumference(self):
    from math import pi
    return 2 * pi * self.radius

  def getRadius(self):
    return self.radius

  def getCenter(self):
    return self.center

  def getX(self):
    return self.center[0]
    
  def getY(self):
    return self.center[1]