import task01, task02, task03

def isInt(val):
  try:
    int(val)
    return True
  except:
    return False

sel = 0
while True:
  sel = int(input("Select task [1..4] -> "))

  if isInt(sel) and 0 < int(sel) < 5:
    break
  
  print("Invalid argument (%s). Try again...\n" % sel)
  

sel = int(sel)

if sel == 1:
  while True:
    sel = int (input("Define ngon side count [3..100] -> "))

    if isInt(sel) and 2 < int(sel) < 101:
      break
    
    print("Invalid argument (%s). Try again...\n" % sel)

  task01.runTask(int(sel))

if sel == 2:
  while True:
    sel = int (input("Define star point count [5..100] -> "))

    if isInt(sel) and 4 < int(sel) < 101:
      break
    
    print("Invalid argument (%s). Try again...\n" % sel)

  task02.runTask(int(sel))

if sel == 3:
  while True:
    sel = int (input("Define n [3..100] -> "))

    if isInt(sel) and 2 < int(sel) < 101:
      break
    
    print("Invalid argument (%s). Try again...\n" % sel)

  k = 0
  while True:
    k = int (input("Define k [1..20] -> "))

    if isInt(k) and 0 < int(k) < 21:
      break
    
    print("Invalid argument (%s). Try again...\n" % k)

  task03.runTask(int(sel), int(k))