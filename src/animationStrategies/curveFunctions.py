



import math


def linear(t: float):
  return t

def easeOut(t: float):
  return t*(-1*t + 2)
  # return math.sqrt(1-(t-1)**2)

def easeIn(t: float):
  return t*t