#   Write a script that guesses the user's imaginary integer. 
#   Initially, the program requires the user to enter the boundaries of the interval in which the 
# imaginary number will be located. The program then outputs a guess. The user must enter: 
# "correct" if the number is guessed correctly; 
# "Too large" if the number is higher than the number of the user; 
# "Too small" if the number is less than the user's number. 
# Guessing is repeated until the number is guessed.
#   Write the fastest guessing algorithm.

print("The program will guess an user-thought number from the interval [m; n].")
print("Enter interval boundaries:")
m = int(input("m <- "))
n = int(input("n <- "))

if m > n:
  temp = m
  m = n
  n = temp

guess = int((m + n) / 2)
run = True

while run:
  print("Thought number is %d? [%d..%d]" % (guess, m, n))

  while True:
    answer = input("<, >, = -> ")

    if answer == "=":
      run = False
      break
    if answer == "<":
      temp = guess
      guess = int((m + guess) / 2)
      n = temp
      break
    if answer == ">":
      temp = guess
      guess = int((guess + n) / 2)
      m = temp
      break

    print("Unknown answer, type < or > or =")