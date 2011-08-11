"""This is Problem 2 of ProjectEuler

Find the sum of all the even-valued terms in the fibonnaci sequence which do not exceed four million."""

__author__ ="Andrew Phoenix"

fib1=1
fib2=1
sum=0

while fib2<4000000:
  increment=fib1+fib2
  fib1=fib2
  fib2=increment
  print fib2
  if fib2%2==0:
    sum=sum+fib2
print sum
