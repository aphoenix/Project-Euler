"""This is Problem 3 of ProjectEuler

find the 1001st prime"""

__author__ = "Andrew Phoenix"


def isprime(n):
    '''Check if integer n is, in fact, prime'''
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


numoprimes = 0

for n in range(1, 1000000):
    if isprime(n):
        numoprimes = numoprimes + 1
    if numoprimes == 10002:
        break
print
n
