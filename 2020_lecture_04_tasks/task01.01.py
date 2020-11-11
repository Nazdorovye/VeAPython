#   Write a script to check the correctness of the user name and password. The program asks you to 
# enter the user name and password, if any of the entered values is incorrect, the program outputs 
# a corresponding message and causes the input to be repeated. 
#   If the user has entered the correct values, the program outputs "Input correct".

while True:
  print("Ievadi lietotāja vārdu:")
  usr = input("==> ")
  print("Ievadi lietotāja paroli:")
  pwd = input("==> ")

  if usr == "user" and pwd == "password":
    print("Paldies! Ievade pareiza.")
    break
  else:
    print("Lietotāja vārds vai parole ievadīti nepareizi. Atkārtojiet ievadi!\n")