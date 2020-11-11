#   Write a script to simulate playing dice
#   1) Die is rolled 10 times. After each roll output resulting value. At the end output the sum 
# of all roll results.
#   2) Two dies are roll 10 times. After each roll output sum of both dice values and the 
# largest of two values. At the end output the sum of all roll largest values.

from random import randint

# die symbol decimal utf-16/32 encoding starts from 9856
def utfDie(num):
  if 0 < num < 7:
    return chr(9855 + num)
  else:
    return "0"


N = 10
history = [0] * N

print("Game #1")
for i in range(N):
  history[i] = randint(1, 6)
  print("#%2d: %s" % (i + 1, utfDie(history[i])))

print("Sum:", end="")
sum = 0
for i in range(N):
  print("%s%d" % ("+ " if i != 0 else " ", history[i]), end=" ")
  sum += history[i]
print("= %d\n" % sum)


history = [[0] * 2 for i in range(N)]

print("Game #2")
for i in range(N):
  history[i][0] = randint(1, 6)
  history[i][1] = randint(1, 6)
  print("#%2d: %s +%s = %d" 
      % (i + 1, utfDie(history[i][0]), utfDie(history[i][1]), history[i][0] + history[i][1]))

print("Sum:", end="")
sum = 0
for i in range(N):
  largest = history[i][0] if history[i][0] > history[i][1] else history[i][1]
  print("%s%d" % ("+ " if i != 0 else " ", largest), end=" ")
  sum += largest
print("= %d\n" % sum)