"""This is Problem 40 of Project Euler

An Irational Number is constructed thus:

0.123456789101112131415161718192021222324252627282930313233...

if d(n) is the nth digit, find d(1)*d(10)*d(100)*d(1000)*d(100000)*d(1000000)"""

__author__ = "Andrew Phoenix"

import eulib

g = eulib.champernowne(1000001)
print
g[1]
print
g[10]
print
g[100]
print
g[1000]
print
g[10000]
print
g[100000]
print
g[1000000]
