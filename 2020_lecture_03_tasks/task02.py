#   Write a script, that asks user to input four integers. The message "ALL EQUAL", "DUPLICATES", 
# "ALL UNIQUE" is then displayed, as appropriate

a = int(input("Type an integer for a -> "))
b = int(input("Type an integer for b -> "))
c = int(input("Type an integer for c -> "))
d = int(input("Type an integer for d -> "))

if a == b == c == d:
  print("ALL EQUAL")
elif a != b and a != c and a != d and b != c and b != d and c != d:
  print("ALL UNIQUE")
else:
  print("DUPLICATES")
