"""This is Problem 30 of Project Euler

Find all the sum of all n such that n is equal to the sum of its digits raised to the power of 5"""

__author__ = "Andrew Phoenix"

import eulib

thegrandtotal = 0
for n in range(2, 1000000):
    if (eulib.sumofpower(n, 5) == n):
        thegrandtotal = thegrandtotal + n
print
thegrandtotal
