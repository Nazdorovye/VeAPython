#   Complete the script written in Task 1.1. If the user name or password is entered incorrectly, 
# the user is prompted and then asked whether to continue entering or end the program. 
#   If the user has chosen to quit, the program outputs: "The program quits". 
#   If the user has entered the correct values, the program outputs: "Input correct".

while True:
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
      print("\n")
      continue
    else:
      print("Programma beidz darbu")
      break
