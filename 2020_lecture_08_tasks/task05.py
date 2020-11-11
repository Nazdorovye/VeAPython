# Define a function that returns hours, minutes and seconds from secons argument

def toHrMinSec(seconds):
  result = [0] * 3

  # divmod returns (x//y, x%y)
  # sec = 3785
  # m, s = 3785 // 60 = 63, 3785 % 60 = 5
  # h, m = 63 // 60   = 1 , 63 % 60   = 3
  result[1], result[2] = divmod(seconds, 60)
  result[0], result[1] = divmod(result[1], 60)

  return result


print("3785 seconds = %s" % toHrMinSec(3785))
print("7205 seconds = %s" % toHrMinSec(7205))
print("13500 seconds = %s" % toHrMinSec(13500))
print("7200 seconds = %s" % toHrMinSec(7200))
print("0 seconds = %s" % toHrMinSec(0))