#   Write a program that prompts the user to enter the number n and then outputs the factorials of 
# all numbers from 1 to n.

n = int(input("Type in n value -> "))

for i in list(range(1, n + 1)):
  fact = 1.

  print("%d! = 1 " % i, end='')
  if i > 1:
    for d in list(range(1, i + 1)):
      fact *= d
      if d != 1: 
        print("* %d " % d, end='')

  print("= %d" % fact)