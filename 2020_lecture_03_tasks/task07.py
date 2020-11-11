#   The script reads four numbers from 1 to 8, where the first two determine the column and row 
# number of the first square the last two determine the column an d row number of the second square.
#   The script outputs "SAME COLOR", if the fields are the same color, or "DIFFERENT COLORS" - if
# otherwise.

# H odd  : W odd - black, even - white
# H even : W odd - white, even - black

W1 = 0
W2 = 0
H1 = 0
H2 = 0

while W1 < 1 or W1 > 8:
  W1 = int(input("Type in first cell horizontal -> "))
if W1 % 2 == 0:
  W1 = False # white
else:
  W1 = True # black

while H1 < 1 or H1 > 8:
  H1 = int(input("Type in first cell vertical -> "))
if H1 % 2 == 0:
  W1 = not W1 # shifts

while W2 < 1 or W2 > 8:
  W2 = int(input("Type in first cell horizontal -> "))
if W2 % 2 == 0:
  W2 = False # black
else:
  W2 = True # white

while H2 < 1 or H2 > 8:
  H2 = int(input("Type in first cell vertical -> "))
if H2 % 2 == 0:
  W2 = not W2 # shifts

if W1 == W2:
  print("SAME COLOR")
else:
  print("DIFFERENT COLORS")