"""This is Problem 10 of ProjectEuler

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

__author__ = "Andrew Phoenix"


def isprime(n):
    '''Check if integer n is, in fact, prime'''
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


primesum = 0

for x in range(2, 2000000):
    if isprime(x):
        primesum = primesum + x

print
primesum
