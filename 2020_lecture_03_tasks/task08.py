#   In chess, the king can only move horizontally, vertically or diagonally by on root per turn.
#   The script reads four numbers from 1 to 8, where the first two determine the column and row 
# number of the first square the last two determine the column an d row number of the second square.
#   The script outputs "CAN" if the king can move from the first square to the second in one move, # or "CAN NOT" - otherwise.

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

if 0 <= abs(W1 - W2) <= 1 and 0 <= abs(H1 - H2) <= 1:
  print("CAN")
else:
  print("CAN NOT")