"""This is Problem 6 of ProjectEuler

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

__author__ = "Andrew Phoenix"

sum1=0
sum2=0
for x in range (1,101):
  sum1=sum1+x**2

for x in range (1,101):
  sum2=sum2+x

print sum1-sum2**2
