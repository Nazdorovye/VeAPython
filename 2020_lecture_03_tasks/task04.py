#   Write a script that does the following:
# 1. Asks the user to enter two numbers. Outputs largest.
# 2. Asks the user to enter three (four) numbers. Outputs largest.
#   Store user defined numbers in separate variables.
#	Use conditional constructions. Do not use iteration structures (cycles) and compound structures, 
# such as lists.
#   Count the largest possible number of comparison operations that must be performed to find the 
# largest number entered. Write the answer in the code comment before performing the comparison
# steps. Design the script in such way that as few comparison steps as possible would be performed.

a = int(input("Type in 1/2 of numbers:"))
b = int(input("Type in 2/2 of numbers:"))

# Largest possible number of comparison operations - 1
if a > b:
  print("Largest is:", a)
else:
  print("Largest is:", b)

a = int(input("Type in 1/3 of numbers:"))
b = int(input("Type in 2/3 of numbers:"))
c = int(input("Type in 3/3 of numbers:"))

# Largest possible number of comparison operations - 2
if a > b:
  if a > c:
    print("Largest is:", a)
  else:
    print("Largest is:", c)
elif b > c:
  print("Largest is:", b)
else:
  print("Largest is:", c)


a = int(input("Type in 1/4 of numbers:"))
b = int(input("Type in 2/4 of numbers:"))
c = int(input("Type in 3/4 of numbers:"))
d = int(input("Type in 4/4 of numbers:"))

# Largest possible number of comparison operations - 3
if a > b:
  if a > c:
    if a > d:
      print("Largest is:", a)
    else:
      print("Largest is:", d)
  elif c > d:
    print("Largest is:", c)
  else:
    print("Largest is:", d)
elif b > c:
  if b > d:
    print("Largest is:", b)
  else:
    print("Largest is:", d)
elif c > d:
  print("Largest is:", c)
else: 
  print("Largest is:", d)