"""This is Problem 16 of ProjectEuler

What is the sum of the digits of the number 21000?
 """

__author__ ="Andrew Phoenix"

x=2**1000
s=str(x)
longlist=[c for c in s]
ints=[int(x) for x in longlist]
print sum(ints)
