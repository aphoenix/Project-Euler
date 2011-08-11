""" This is Problem 12 of Project Euler.

What is the first triangle number to have over 500 divisors?

Note that the first number to have 500 divisors is 62370000.
The first Triangle number that is bigger than that is the 11169th triangle number: 62378865

"""

__author__ = "Andrew Phoenix"

import eulib

'''the first number with 500 divisors is 62370000 a triangular number near there is tri(3531)'''

x=3531

while len(eulib.divisors(eulib.gentri(x)))<500:
    x=x+1
print eulib.gentri(x)
