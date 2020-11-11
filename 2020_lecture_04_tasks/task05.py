#   Write a script that determines whether a number is a prime number or not. 
#   Print all primes from the interval [1; 𝑛] (n entered by the user).

n = int(input("Type in n value -> "))
print("Primes [1..n]: ", end="")
for i in list(range(1, n)):
  for j in list(range(2, i - 1)):
    if i % j == 0:
      break
  else:
    print("%s%d" % (", " if i != 1 else "", i), end="")

print("")