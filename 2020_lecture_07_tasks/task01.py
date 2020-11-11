#   Write a script that fills the list with length (𝑁 = 10) with integer random numbers from the 
# interval [1; 100]. 
#   Then output: 
#   1) all list items 
#   2) all list items in reverse order 
#   3) all even index elements (0 will be considered an even number) 
#   4) all list items whose value is an even number 
#   5) the sum of list items 
#   6) the alternate sum of list items, i.e. each the second element, taking the opposite sign, for 
# example, the alternate sum of the elements 
#       [1, 4, 9, 16, 9, 7, 4, 9, 1] is 
#       1 - 4 + 9 - 16 + 9 - 7 + 4 - 9 + 11 = -2

import random

N = 10
nums = [random.randint(1, 100) for x in range(N)]

print("1. list elements are: ", end="")
for i in range(N):
  print("%s%d" % (", " if i != 0 else "", nums[i]), end="")

print("\n2. reverse list elements are: ", end="")
for i in range(N)[::-1]:
  print("%s%d" % (", " if i != 9 else "", nums[i]), end="")

print("\n3. even index elements are: ", end="")
for i in range(N):
  if i % 2 == 0:
    print("%s%d" % (", " if i != 0 else "", nums[i]), end="")

sum = 0
altsum = 0
lst = 0
positive = True

print("\n4. even elements are: ", end="")
for i in range(N):
  sum += nums[i]

  # swap sign for every second element
  altsum = altsum + nums[i] if positive else altsum - nums[i]
  positive = not(positive)
  
  if nums[i] % 2 == 0:
    print("%s%d" % (", " if lst != 0 else "", nums[i]), end="")
    lst += 1

print("\n5. list element sum is: %d" % sum, end="")
print("\n6. list element alternating sum is: %d" % altsum, end="")
print("")