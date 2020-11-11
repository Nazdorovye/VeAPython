#   Write a script that generates random numbers from the interval [1; 10] and writes them to a 
# list (the number count is determined by the programmer, for example 20). The entered values may 
# be repeated. Print this list. 
#   Then copy values in the other list without repetitions (unique values only). Arrange them in 
# ascending order. Print this list. 
#   Output the number of repetitions of each value in the first list. 
#   Create a histogram - a graph showing the number of iterations of a value. The bars in the chart 
# are formed by output a row of symbols of the appropriate length.

import random

N = 20
nums = [random.randint(1, 10) for i in range(N)]

print("num list elements are: ", end="")
for i in range(N):
  print("%s%d" % (", " if i != 0 else "", nums[i]), end="")

uniq = []

for i in nums:
  if len(uniq) == 10:
    break

  if i not in uniq:
    uniq.append(i)

uniq.sort()

print("\nuniq list elements are: ", end="")
for i in range(len(uniq)):
  print("%s%d" % (", " if i != 0 else "", uniq[i]), end="")

print("\nnum list element histogram:", end="")
for i in range(10):
  print("\n%02d | " % (i + 1), end="")

  for j in nums:
    if i + 1 == j:
      print("*", end="")

print("")