#   Write a script that reads a set of floating-point data values. Choose an appropriate mechanism
# for prompting for the end of the data set.
#   When all values have been read, print out the count of the values, the mean and the standard
# deviation.
#   The mean of a data set {x1, ..., xn} is avg(x) = ∑xi/n, where ∑xi = x1 + ... + xn is the sum 
# of the input values.
#   The standard deviation is s = sqrt( ∑(xi - avg(x))^2 / (n-1) )
#   However, this formula is not suitable for the task. By the time the program has computed avg(x),
# the individual xi are long gone. Until you know how to save these values, use the numericaly less
# stable formula s = sqrt( (∑xi^2 - (1/n)*(∑xi)^2) / (n - 1) ).
#   You can compute this quantity by keeping track of the count, the sum, and the sum of squares as
# you process the input values.
#
#   -Vitola:
#   * Use the Python List to store entered numbers
#   * Since this is a learning exercise, calculate the standard deviation using both formulas.
# Compare and output both results.

def isFloat(val):
  try:
    float(val)
    return True
  except:
    return False

print("Enter set of numbers separated by comma (','), i.e. 15, -58.6, asd = [15.0, -58.6] ")
inbuf = input("-> ").split(",")
sum = 0.

idx = 0
while idx < len(inbuf):
  if isFloat(inbuf[idx]):
    inbuf[idx] = float(inbuf[idx])
    sum += inbuf[idx]
  else:
    del inbuf[idx] # not float, delete element
    continue # inbuf shrinks, leave idx as is to stay in bounds
  idx += 1

avg = sum / len(inbuf)
sumsqr = (sum**2) / len(inbuf) # (1/n)*(∑xi)^2)

print("Correct float value count: %d" % len(inbuf))
print("Mean: %f" % avg)

sum = 0.
sqrsum = 0. # ∑xi^2

for elm in inbuf:
  sum += (elm - avg)**2
  sqrsum += elm**2

stdev = (sum / (len(inbuf) - 1))**0.5
stdev2 = ((sqrsum - sumsqr) / (len(inbuf) - 1))**0.5

print("True stdDev: %f" % stdev)
print("Approx stdDev: %f" % stdev2)
print("Difference: %f" % (stdev - stdev2))