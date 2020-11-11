#   Write a script that calculates roots of an quadratic equation. Coefficients to be typed by user.
#   Depending on the number of real roots, the script outputs one or  two real roots of the 
# quadratic equation. If the equation has no real roots, the script outputs according message.

a = float(input("Type in coeff a -> "))
b = float(input("Type in coeff b -> "))
c = float(input("Type in coeff c -> "))

discr = b*b - 4 * a * c
print("D =", discr)

if discr < 0:
  print("No real roots!")
elif discr == 0:
  print("x = ", -b / 2 * a)
else:
  print("x1 = ", (-b + (b*b - 4 * a * c)**0.5) / (2 * a))
  print("x2 = ", (-b - (b*b - 4 * a * c)**0.5) / (2 * a))
