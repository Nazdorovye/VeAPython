#   There are well-known algorithms for finding the highest and lowest values in a list. Using 
# these algorithms, perform the task described below. 
#   There are two lists of length 10, in which the x and y coordinates of the points are recorded, 
# respectively. The lists are filled in by generating random integer values from the interval 
# [−10; 10] with the help of a random number generator.
#   1) Find the coordinates and area of the bounding box that can be drawn for these points.
#   2) Output the values of the elements of the array as pairs of point coordinates: (𝑥𝑖, 𝑦𝑖).
#   3) Output the coordinates of the corners of the rectangle as pairs of point coordinates.
#   4) Output the area of the rectangle.
#   5) Find and output the bounding circle radius and area.

import random
import math

N = 10
xn = [random.randint(-10, 10) for i in range(N)]
yn = [random.randint(-10, 10) for i in range(N)]

# Bounding box edges
bbx = min(xn), max(xn)
bby = min(yn), max(yn)

# Bounding box vertices
vert =  [ (bbx[0], bby[0]), (bbx[0], bby[1]), (bbx[1], bby[1]), (bbx[1], bby[0]) ]

# Bounding box area
A = (bbx[1] - bbx[0]) * (bby[1] - bby[0])

# All (x, y) coordinate pairs
xyn = list(zip(xn, yn))

print("\n2. All point coords (xi, yi): ", xyn)
print("3. Bounding box vertex coordinates: ", vert)
print("4. Bounding box area: ", A)

# Bounding circle coordinates
bc = float((bbx[0] + bbx[1]) / 2.), float((bby[0] + bby[1]) / 2.)

# Bounding circle radius
r = 0.   # largest r from c(bc[0],bc[1])

for i in range(N):
  rt = ((xn[i] - bc[0])**2 + (yn[i] - bc[1])**2)**.5

  if rt > r:
    r = rt

print("5. Bounding circle radius: %.2f" % r)

# Bounding circle area
print("   Bounding circle area: %.2f" % (math.pi * r**2))

print("")

