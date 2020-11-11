#   Write a script that requires the user to enter five characters. After each mark entered, the 
# program checks whether the mark has been entered correctly (the mark can be from 1 to 10). 
#   This time we will not check if the entered value is an integer. 
#   When five correct marks are entered, the program outputs the average mark. 
#   Use repeat instructions while.

i = 0
avg = 0

while i < 5:
  tmp = int(input("Ievadi atzīmi: "))
  if 0 < tmp < 11:
    avg += tmp
    i += 1
  else:
    print("Mēģini vēlreiz!\n")

print("Vidējā atzīme ir", avg / 5)
