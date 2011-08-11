"""This is Problem 48 of Project Euler

Find the last 10 digits of 1^1 + 2^2 + 3^3 + ... + n^n + ... + 1000^1000"""

__author__ = "Andrew Phoenix"

x = 1
p = 0


while x < 10:
    p += x**x
    x += 1


print p
print x

x = 11


while x < 1000:
    if x%10 != 0:
        p += x**x
        p = p%10000000000
    x += 1
    print p

        
