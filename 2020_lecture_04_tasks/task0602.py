#   Write a script in which the user has to guess a computer generated random number in the 
# interval [1, n] where n is entered by the user. 
#   The computer outputs: "correct" if the number is guessed correctly; 
#   "Too large" if the number is greater than the computer number. 
#   "Too small" if the figure is less than computer number. 
# Repeat until the number is guessed. 
# At the end of the program, the number of guesses is output.

import random

print("The program will randomize an integer in the interval [1; x].")
print("Type in guessing boundary [1..x]")
n = random.randint(1, int(input("x -> ")))

i = 0

while True:
  i += 1 
  guess = int(input("Guess the number -> "))

  if guess < n:
    print("%d < x" % guess)
    continue
  if guess > n:
    print("%d > x" % guess)
    continue
  if guess == n:
    print("CORRECT! Guess count: %d" % i)
    break

