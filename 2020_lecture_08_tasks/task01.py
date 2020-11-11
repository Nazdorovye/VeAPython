#   Define a function that returns bool if attribute a divides evenly by attibute b

from random import randint


def isNumerical(val):
  try:
    int(val)
    return True
  except:
    print("%s not numerical" % val)
    return False

def divHasRemainder(a, b):
  if isNumerical(a) and isNumerical(b) and b != 0:
    return not bool(float(a) % float(b))


print(" a  /  b  | has remainder")
print("-------------------------")
print("%3d / %3d | %s" % (98, 7, divHasRemainder(98, 7)))
print("%3d / %3d | %s" % (85, 4, divHasRemainder(85, 4)))

for i in range(10):
  a = randint(0, 10)
  b = randint(1, 10)

  # when b > a, b / a will always have a remainder, not taking into account
  if b > a: a, b = b, a

  print("%3d / %3d | %s" % (a, b, divHasRemainder(a, b)))