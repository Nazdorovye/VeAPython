#   There is a list with integers and two separate sets s0 and s1, each of which contains integers. 
# Jānītis likes all the s0 ints and does not like all the s1 ints. 
#   Jānītis initial happiness index is 0. 
#   For each integer from the array:
#     if 𝑖 ∈ s0, the happiness index must be incremented;
#     if 𝑖 ∈ s1, the happiness index must be decremented; 
#     if default, the happiness index is not changed. 
#   Because s0 and s1 are sets, they do not have repeating elements, and the array may contain 
# repeating values. In the program it is desirable to use the functions designed to work with sets.
#
#   Perform the following actions in the program:
#     1. Create a list with n (𝑛 = 6) integer random numbers from the interval [1; 10].
#     2. Create two sets s0 and s1 with m (𝑚 = 3) elements, where each set element belongs to the 
# interval [1; 10]. To obtain two separated sets in the program, the following algorithm is 
# implemented:
#       1) create a set s2 with all numbers from 1 to 10 (use a range object).
#       2) create set s0 - use the sample function from the module random, which returns a list of 
# k random elements from a sequence or set of numbers (uses the set s2 created in point 1).
#       3) create the set s1 - use the sample function, which returns a list of k random elements 
# from a sequence or set of numbers. To make the elements of the set s1 different from the elements 
# of the set s0, the difference between sets s2 and s0 is used as the argument to the sample 
# function.
#     3. Calculates the happiness index.
#     4. Outputs the list, both sets and the happiness index.

from random import randint, sample


N = 6
M = 3

lst = [randint(1, 10) for i in range(N)]
print("\nIndex list: ", lst)

s1 = set(range(1, 11))
s0 = set(sample(s1, M))
s1 = set(sample(s1 - s0, M))
print("Set A: ", s0)
print("Set B: ", s1)


hapIdx = 0 # happiness index

for elm in lst:
  if elm in s0:
    hapIdx += 1
  elif elm in s1:
    hapIdx -= 1

print("Happiness index: %d\n" % hapIdx)