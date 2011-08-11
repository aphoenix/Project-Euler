"""This is Problem 1 of ProjectEuler

Find the sum of the digits in the number 100!"""

__author__ ="Andrew Phoenix"

import math

x=math.factorial(100)
print x

s=str(x)
longlist=[c for c in s]
ints=[int(x) for x in longlist]
print sum(ints)
