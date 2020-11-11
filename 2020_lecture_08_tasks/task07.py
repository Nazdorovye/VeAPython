#   Write a script to simulate playing dice.
#   Game rules:
#   1) Two players are participating in the game. "Player 1" starts the game.
#   2) Each of the player throws two dies in his turn. Resulting die sum adds up to player score.
#   3) The game ends when any player reaches 100-point score and becomes a winner.
#   After each turn output roll result and accumulated score of the player.
#   1*) Evaluate the ability to define functions for individual tasks. Define functions as you see 
# fit, but always follow good programming practices.
#   2*) Complete the game with the following scoring rules: 
#     -if the player throws the same number of points for both dice (except for two singles), the 
# amount of points obtained in this turn doubles;
#     -if the player throws exactly one single, he loses the points obtained in the turn;
#     -if the player throws two singles, he loses both the points scored in the turn and all the 
# points previously earned.
#   3*) In the previous version, the game was always started by "Player 1". Modify the program so 
# that the initiator of the game is identified by the heads or tails game.

from random import randint

names = ["Player", "Rival "]
scores = [0] * 2
rollD1 = 0
rollD2 = 0
rollScore = 0
currPlayer = 0

def playerRoll(rollNum):
  global currPlayer

  currPlayer = 1 - currPlayer
  scoreAmendments()

  print("%s roll #%2d: %s +%s = %3d\t| Score: %3d" 
      % (names[currPlayer], rollNum, utfDie(rollD1), utfDie(rollD2), rollScore, 
         scores[currPlayer]))

  if scores[currPlayer] >= 100:
    return True
  return False

def scoreAmendments():
  global rollD1, rollD2, rollScore, scores

  rollD1 = randint(1, 6)
  rollD2 = randint(1, 6)

  # Checks if there is exactly one die with single
  if ((rollD1 == 1 and rollD2 != 1) or (rollD2 == 1 and rollD1 != 1)):
    rollScore = 0
  # If both dies are single
  elif (rollD1 == rollD2 == 1):
    rollScore = -scores[currPlayer]
  # If both dies are equal but not single
  elif (rollD1 == rollD2):
    rollScore = (rollD1 + rollD2)*2
  else:
    rollScore = rollD1 + rollD2
    
  scores[currPlayer] += rollScore

# die symbol decimal utf-16/32 encoding starts from 9856
def utfDie(num):
  if 0 < num < 7:
    return chr(9855 + num)
  else:
    return "0"



# Define who is rolling first
answer = 0

while True:
  answer = input("Choose heads or tails to define the first player [H/t] -> ").lower()
  if answer == "h" or answer == "": 
    answer = 0
    break
  elif answer == "t":
    answer = 1
    break

  print("Unknown input ('%s'). Try again" % answer)

currPlayer = int(answer == randint(0, 1))
print("\n\n%s starts first!\n" % names[1 - currPlayer])



# Game loop
iLoop = 0
while True:
  iLoop += 1
  
  if playerRoll(iLoop):
    break
  if playerRoll(iLoop):
    break
  print()

print("\n%s won!\n\n" % names[currPlayer])