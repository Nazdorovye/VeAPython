#   Complete the script written in Exercise 1.2. If the user name or password is entered 
# incorrectly five times, the program will issue a message and stop working.

i = 5
while i > 0:
  print("Ievadi lietotāja vārdu:")
  usr = input("==> ")
  print("Ievadi lietotāja paroli:")
  pwd = input("==> ")

  if usr == "user" and pwd == "password":
    print("Ievade pareiza")
    break
  else:
    ans = input("Ievade nepareiza.Vai vēlaties atkārtot? (yY == Jā) -> ")
    if ans.lower() == 'y':
      i -= 1
      print("\n")
      continue
    else:
      break
else:
  print("\nNepareizi ievadīts 5 reizes. Programma beidz darbību!")

