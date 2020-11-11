#   Define a function that returns the sum of latin alphabet symbols of the argument string
#   ASCII a = 097 .. z = 122

DEF_SYM_OFFSET = 96
DEF_SYM_LO = 97
DEF_SYM_HI = 122

def sumLatinSymbols(string):
  lower = str(string).lower()
  result = 0

  for i in range(len(lower)):
    sym = ord(lower[i])

    if DEF_SYM_LO <= sym <= DEF_SYM_HI:
      result += sym - DEF_SYM_OFFSET

  return result


print("COLIN = %d" % sumLatinSymbols("COLIN"))
print("Ace = %d" % sumLatinSymbols("Ace"))
print("cloud = %d" % sumLatinSymbols("cloud"))