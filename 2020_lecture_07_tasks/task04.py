#   Enter a four-digit number with at least two different digits in the variable. 
#   The program must arrange the digits of this number in ascending and descending order. Then 
# subtract the smallest from the largest number. Then repeat the previous steps until a fixed 
# number is reached: 6174. 
#   By performing the above steps with the number 6174, the result is again 6174 (7641-1467=6174). 
#   The program must read a four-digit number. You must output how many times the algorithm was
# repeated to reach the number 6174. For example, if you enter the number 3524, the program must 
# output 3 because the program performs the following steps: (1) 5432 - 2345 = 3087, 
# (2) 8730 - 0378 = 8352, (3 ) 8532 - 2358 = 6174.

def isNum(val):
  try:
    int(val)
    return True
  except:
    return False

print("Type four digit number. First 4 digits will be taken from the input string.")
num = list(input("-> "))

idx = 0
while idx < len(num):
  if not isNum(num[idx]) or idx >= 4:
    del num[idx] # not a digit, remove
    continue # num shrinks, leave idx as is to stay in bounds
  idx += 1

idx = 0
while True:
  idx += 1

  num.sort()
  min = int("".join(num))
  num.reverse()
  max = int("".join(num))

  res = max - min
  print("%d | %d - %d = %d" % (idx, max, min, res))

  if res == 6174:
    break

  num = list(str(res).zfill(4))

print("Calculations took %d steps" % idx)