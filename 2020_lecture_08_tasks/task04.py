#   Define a function that returns seconds from hour, minute and second arguments

def toSeconds(h, m = 0, s = 0):
  return h * 3600 + m * 60 + s


print("01 hours 03 minutes and 05 seconds = %d" % toSeconds(1, 3, 5))
print("02 hours and 05 seconds = %d" % toSeconds(2, 0, 5))
print("03 hours and 45 minutes = %d" % toSeconds(3, 45))
print("02 hours = %d" % toSeconds(2))
print("00 hours = %d" % toSeconds(0))