"""This is Problem 1 of ProjectEuler

Find the sum of all natural numbers between 1 and 1000 that are multiples of 3 and 5"""

__author__ = "Andrew Phoenix"

f = 0
x = 1
while x < 1000:
    if x % 3 == 0:
        f = f + x
    elif x % 5 == 0:
        f = f + x
    x = x + 1
print
f
