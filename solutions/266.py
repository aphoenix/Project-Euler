"""This is Problem 266 of ProjectEuler

Of PseudoPrimes and modular arithmetic

Pseudo Square Root (PSR) is the largest proper divisor that does not exceed the square root.

Let p be the product of the primes below 190.

Find PSR(P) mod 10^16

http://projecteuler.net/index.php?section=problems&id=266"""


import eulib
import math


p = 1

for x in range (2, 190):
  if eulib.isprime(x):
    p = p * x

top=int(math.sqrt(p))

# having run this before, with print debug statements, I've seen that top = 2323218950681478489303377251995413046 is appropriate

top = 2323218950681478489303377251995413046

while top%p != 0:
    top -= 1
    print top

print top%10**16
