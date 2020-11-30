from typing import Match


from math import gcd

class fraction:
  def __init__(self, numerator: int = 0, denominator: int = 1):
    __gcd = gcd(numerator, denominator)
    self.numerator = numerator // __gcd
    self.denominator = denominator // __gcd

    if self.denominator < 0:
      if self.numerator < 0:
        self.denominator = abs(self.denominator)
        self.numerator = abs(self.numerator)
      else:
        self.numerator = -self.numerator
        self.denominator = abs(self.denominator)

  def __add__(self, other):
    return fraction(
      self.numerator * other.getDenominator() + other.getNumerator() * self.denominator,
      self.denominator * other.getDenominator())

  def __sub__(self, other):
    return fraction(
      self.numerator * other.getDenominator() - other.getNumerator() * self.denominator,
      self.denominator * other.getDenominator())

  def __mul__(self, other):
    return fraction(self.numerator *other.getNumerator(), self.denominator * other.getDenominator())

  def __truediv__(self, other):
    return fraction(self.numerator *other.getDenominator(), self.denominator * other.getNumerator())

  def __lt__(self, other) -> bool:
    return self.numerator * other.getDenominator() < self.denominator * other.getNumerator()

  def __gt__(self, other) -> bool:
    return self.numerator * other.getDenominator() > self.denominator * other.getNumerator()

  def __eq__(self, other) -> bool:
    return self.numerator * other.getDenominator() == self.denominator * other.getNumerator()

  def __ne__(self, other) -> bool:
    return self.numerator * other.getDenominator() != self.denominator * other.getNumerator()

  def __float__(self):
    return self.numerator / self.denominator

  def __int__(self):
    return self.numerator // self.denominator

  def __str__(self):
    return str.format(str(self.numerator)+ "/"+ str(self.denominator))

  def getNumerator(self):
    return self.numerator

  def getDenominator(self):
    return self.denominator