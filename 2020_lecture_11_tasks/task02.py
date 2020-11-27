#   Write a class Circle Client script. Create a list of 10 circles. The coordinates and radius of 
# the circle center are integer random numbers from the given interval (coordinates - [- 50; 50]; 
# radius - [1; 10]). 
#   Output the existing circles in the circle list (center coordinates and radius). Also output the 
# distance of each circle to the origin of the coordinates. 
#   Find the circle closest to the starting point of the coordinates. Remove this circle and its 
# distance to the origin of the coordinates.

import circle
from random import randint

from circle import Circle

C_MIN = -50
C_MAX = 50
R_MIN = 1
R_MAX = 10
CIRC_CNT = 10

c_lst = [
  Circle((randint(C_MIN, C_MAX), randint(C_MIN, C_MAX)), randint(R_MIN, R_MAX)) 
  for c in range(CIRC_CNT)
  ]

c_closest_idx = 0
for i in range(len(c_lst)):
  print("#%d: %s;\tDistance to (0, 0): %.2f" % (i + 1, c_lst[i].__str__(), c_lst[i].distance()))

  if c_lst[i].distance() < c_lst[c_closest_idx].distance():
    c_closest_idx = i

print("\nClosest circle to (0, 0) is: #%d: %s;\tDistance to (0, 0): %.2f" % 
  (c_closest_idx + 1, c_lst[c_closest_idx].__str__(), c_lst[c_closest_idx].distance()))
  