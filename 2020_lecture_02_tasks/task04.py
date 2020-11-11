#   Write a script, that calculates and outputs volume and  surface area for a sphere with R-radius 
# (input by user).
#   PI could be defined as const, or used from math module implementation.

PI = 3.14159265358979

r = float(input("Type in sphere radius -> "))

print("Sphere volume is:", 1.33333333333*PI*r**3)
print("Sphere surface area is: ", 4*PI*r*r)