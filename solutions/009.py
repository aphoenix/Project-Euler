"""This is Problem 9 of ProjectEuler

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

__author__ = "Andrew Phoenix"

# a    + b    + c   = 1000
# a**2 + b**2       = c**2
# c    = 1000 - a - b
# c**2 = (1000 - a - b)(1000 - a - b)

# a=1000(b-500)/(b-1000)

# find the roots: a=200 b=375
# then c = 425

print
200 * 375 * 425
