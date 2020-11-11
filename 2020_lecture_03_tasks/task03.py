#   Write a script that determines whether a triangle can be created from user-entered edge 
# lengths. If it can, calculate and output the area and perimeter of this triangle. 
#   Condition for creating a triangle: the sum of any two sides is greater than the third side.

a = float(input("Type the length for the edge a -> "))
b = float(input("Type the length for the edge b -> "))
c = float(input("Type the length for the edge c -> "))

if a + b > c and b + c > a and c + a > b:
  print("Area of specified triangle is:", (a + b + c) / 2)
  print("Perimeter of the triangle is:", a + b + c)
else:
  print("Triangle cannot be built with a=%.2f b=%.2f c=%.2f" % (a, b, c))