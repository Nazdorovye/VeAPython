#   Define a function that returns subtract between argument list max and min

from random import randint

def diffMaxMinList(lst):
  min = lst[0]
  max = lst[0]

  for elm in lst:
    if elm < min: min = elm
    if elm > max: max = elm

  return max - min


lst = [10, 4, 1, 4, -10, -50, 32, 21]
print("max - min = %d\t|<- %s" % (diffMaxMinList(lst), lst))

lst = [44, 32, 86, 19]
print("max - min = %d\t|<- %s" % (diffMaxMinList(lst), lst))

for i in range(10):
  lst = [randint(-50, 50) for j in range(randint(2, 10))]

  print("max - min = %d\t|<- %s" % (diffMaxMinList(lst), lst))