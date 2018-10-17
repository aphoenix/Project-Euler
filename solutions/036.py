"""For solving Problem 36 of Project Euler:

Find the sum of all numbers below dec(1000000) that are palindromes in dec and bin."""

__author__ = "Andrew Phoenix"

import eulib

sum = 0
for n in range(0, 1000000):
    if eulib.ispalindrome(n):
        if eulib.ispalindrome(eulib.dectobin(n)):
            sum = sum + n
            print
            sum
