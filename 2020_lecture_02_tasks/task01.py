#   Write a script which asks user to type in two numbers - x and y, and then calculates following 
# formulas:
# 1. (2+x)/xy
# 2. 5(x^3)-(x^2)+7x-6
# 3. sqrt(xy)

# Do not use Python library functions!

x = float(input("Type in x variable -> "))
y = float(input("Type in y variable -> "))

print("(2+x)/xy =", (2+x)/(x*y))
print("5(x^3)-(x^2)+7x-6 =", 5*(x**3)-x*x+7*x-6)
print("sqrt(xy) =", (x*y)**(.5))