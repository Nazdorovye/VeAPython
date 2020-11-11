#   Matrices in programming are represented by two-dimensional arrays or other data containers. 
# This time we will use lists to represent the matrices. 
#   Create two two-dimensional lists (𝑁 × 𝑁, 𝑁 = 3). 
#   Fill them with random numbers from the interval [1; 10].
#   Output both lists (matrices) in tabular form. 
#   Find the sum of both matrices, output the sum in table form. 
#   Multiply the matrix by a number, output in table form. 
#   Find the product of both matrices, output the product of the multiplication in table form.

import random

def isNum(val):
  try:
    int(val)
    return True
  except:
    return False

while True:
  print("Enter a number to multiply:")
  
  num = input("-> ")
  if isNum(num):
    num = int(num)
    break

  print("Not integer. Try again\n")

N = 3

M1 = [ [random.randint(1, 10) for j in range(N)] for i in range(N) ]
M2 = [ [random.randint(1, 10) for j in range(N)] for i in range(N) ]
Msum = [ [M1[i][j] + M2[i][j] for j in range(N)] for i in range(N) ]
Mmul = [ [Msum[i][j] * num for j in range(N)] for i in range(N) ]

print("    M1:\t\t    M2:\t\t    Msum:\t   Msum *", num, ":")
for i in range(N):  
  print(M1[i], "\t", M2[i], "\t", Msum[i], "\t", Mmul[i])

MxM = [ [0] * 3 for i in range(N) ]

for i in range(3):
  for j in range(3):
    for k in range(3):
      MxM[i][j] += M1[i][k] * M2[k][j]

print("\n  M1 x M2:")

for i in range(3):
  print(MxM[i])