from circle import Circle
from point import Point
from random import randint

RC = 200
HW = 250
HH = HW
POINTS = 20

crcl = Circle((0, 0), RC)
points = [Point((randint(-HW, HW), randint(-HH, HH))) for _ in range(POINTS)]

print("Canvas bounds <(x0=%d, x1=%d)(y0=%d, y1=%d)>" % (-HW, HW, -HH, HH))
print("Bounding circle %s", crcl)
print("Points:")

idx = 0
for p in points:
  dist = p.distance(crcl)
  print("#%d: %s, distance: %d, inside: %s" % (idx, p, dist, dist <= crcl.radius))
  idx += 1