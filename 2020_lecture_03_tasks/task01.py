#	  Write a script, that asks user to type in coordinates of a point. Output whether the point is 
# in the given area or outside it.
#	  2 <= x <= 6 ; 1 <= y <= 3
#	Use only one conditional expression

x = float(input("Type in x coordinate -> "))
y = float(input("Type in y coordinate -> "))

if 2 <= x <= 6 and 1 <= y <= 2:
  print("x=%.2f and y=%.2f are located in given area!" % (x, y))
else:
  print("x=%.2f and y=%.2f are located outside given area!" % (x, y))
