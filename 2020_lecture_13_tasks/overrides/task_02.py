from Fraction import fraction

n1 = fraction(16, -9)
n2 = fraction(-4, -16)
n3 = fraction(3)
n4 = fraction()
n5 = fraction(3, 0)

print("n1 = ", n1)
print("n2 = ", n2)
print("n3 = ", n3)
print("n4 = ", n4)
print("n5 = ", n5)

print("n1 + n2 = %s" % (n1 + n2))
print("n2 - n3 = %s" % (n2 - n3))
print("n3 * n4 = %s" % (n3 * n4))
print("n4 / n5 = %s" % (n4 / n5))

print("n1 > n2 = %s" % (n1 > n2))
print("n2 < n3 = %s" % (n2 < n3))
print("n3 == n4 = %s" % (n3 == n4))
print("n4 != n5 = %s" % (n4 != n5))