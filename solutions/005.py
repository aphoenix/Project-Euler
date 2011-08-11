"""This is Problem 5 of ProjectEuler

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?"""

__author__ = "Andrew Phoenix"

def checkdiv(x):
  for p in range (1,20):
    if not x%p==0:
      return False
  return True

x=2520*11*13*17*19*2
print x

for p in range (1,21):
  if x%p==0:
    print p

