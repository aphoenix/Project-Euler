"""For solving Problem 282 of Project Euler: the infamous Ackermann"""

__author__ = "Andrew Phoenix"

import eulib

sum=eulib.ackermann(0,0)
print sum
sum=sum+eulib.ackermann(1,1)
print sum
sum=sum+eulib.ackermann(2,2)
print sum
sum=sum+eulib.ackermann(3,3)
print sum
