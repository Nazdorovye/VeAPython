#   In chess, the tower can only move horizontally or vertically.
# The script reads four numbers from 1 to 8, where the first two determine the column and row 
# number of the first square the last two determine the column an d row number of the second square.
#   The script outputs "CAN" if tower can move from the first square to the second in one move, or 
# "CAN NOT" - if otherwise.

W1 = 0
W2 = 0
H1 = 0
H2 = 0

while W1 < 1 or W1 > 8:
  W1 = int(input("Type in first cell horizontal -> "))

while H1 < 1 or H1 > 8:
  H1 = int(input("Type in first cell vertical -> "))

while W2 < 1 or W2 > 8:
  W2 = int(input("Type in first cell horizontal -> "))

while H2 < 1 or H2 > 8:
  H2 = int(input("Type in first cell vertical -> "))

if H1 == H2 or W1 == W2:
  print("CAN")
else:
  print("CAN NOT")