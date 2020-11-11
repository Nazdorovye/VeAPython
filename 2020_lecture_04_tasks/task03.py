#   Find different amounts. Use iteration for.
#   3.1. The sum of the numbers from 1 to n (n is entered by the user).
#   3.2. The sum of even numbers from 2 to n (n is entered by the user).
#   3.3. The sum of odd numbers from 1 to n (n is entered by the user).
#   3.4. 1 + 1/1! +1/2! +1/3! + ... + 1/𝑛! (n is entered by the user).

n = int(input("Type in n value -> "))
sm = 0
smeven = 0
smodd = 0
fact = 1.0

for i in list(range(1, n + 1)):
  sm += i       # 3.1

  if i % 2 == 0:
    smeven += i # 3.2
  else:
    smodd += i  # 3.3

  div = 1.      # 3.4

  if i > 1: # factorial n!
    for d in list(range(1, i + 1)):
      div *= d

  fact += 1. / div

print("Sum from 1 to %d: %d" % (n, sm))
print("Sum of even from 1 to %d: %d" % (n, smeven))
print("Sum of odd from 1 to %d: %d" % (n, smodd))
print("Fact func of from 1 to %d: %f" % (n, fact))