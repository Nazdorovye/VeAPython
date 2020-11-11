#   Write a script, that swaps values of two variables a and b
# 1. Use traditional temp var
# 2. Use calculations, no temp var
# 3. Use Python method

a = 4
b = 5

print("a =", a, "b =", b, "swapping w/ temp var method...")

temp = a
a = b
b = temp

print("a =", a, "b =", b, "swapping w/ calc method...")

a = a + b # a = 5 + 4 = 9
b = a - b # b = 9 - 4 = 5
a = a - b # a = 9 - 5 = 4

print("a =", a, "b =", b, "swapping w/ Python method...")

a, b = b, a

print("a =", a, "b =", b)