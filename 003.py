"""This is Problem 3 of ProjectEuler

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 """

__author__ ="Andrew Phoenix"

import math

x=600851475143

def isprime(n):
  '''Check if integer n is, in fact, prime'''
  for p in range (2, int(n**0.5)+1):
    if n%p==0:
      return False
  return True

def modulo(n,p):
  '''check if n is divisible by p'''
  check=n%y
  if check == 0:
    return True
  else:
    return False

def countdown(x):
  '''Find the prime divisors of x'''
  for p in range(1, int(x**0.5)+1):
    if isprime(p):
      if x%p==0:
        print p

countdown(x)
    
