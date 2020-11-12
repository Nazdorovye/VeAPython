#   Python sets have a defined function pop() that removes an arbitrary element from the set and 
# returns it. Applying the pop() function to an empty set causes an error. 
#   Also, operators in and not in are defined for sets to check if an element is in set. 
#   Create a set by entering 10 random int values from the interval [1; 20]. 
#   Note that only unique values will be stored in set. 
#   Output the set to see its contents. 
#   For numbers from 1 to 20 check if they are in set or not.

from random import randrange

s0 = []

while len(s0) < 10:
  n = randrange(1, 20)

  if n not in s0:
    s0.append(n)

s0 = set(s0)
print("s0 = ", s0)

print()
for num in range(1, 20):
  print("%d - %sin set" % (num, "" if num in s0 else "not "))

print()
while len(s0) > 0:
  print("popped ", s0.pop())