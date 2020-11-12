#   Define two random long strings. Output 'em.
#   Cast strings to sets. Output 'em.
#   By using defined methods of sets, oputput new sets of set:
#     union, 
#     intersection, 
#     complement, 
#     symmetric difference.

from random import randint

def randChar():
  if randint(0, 1):
    return chr(randint(65, 90)) # uppercase
  else:
    return chr(randint(97, 122)) # lowercase


s0 = "".join(randChar() for rng in range(20))
s1 = "".join(randChar() for rng in range(20))

print("s0 = ", s0)
print("s1 = ", s1)

# cast to set
s0 = set(s0)
s1 = set(s1)

print("s0 = ", s0)
print("s1 = ", s1)

# set operations
print("s0 ∪ s1 = ", set.union(s0, s1))
print("s0 ∩ s1 = ", set.intersection(s0, s1))
print("s0 \ s1 = ", set.difference(s0, s1))
print("s0 Δ s1 = ", set.symmetric_difference(s0, s1))