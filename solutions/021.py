"""This is Problem 21 of Project Euler

Find the sum of all amicable numbers under 10000

An amicable pair is define as m,n such that the proper divisors of m sum 
to n and the proper divisors of n sum to m"""

__author__ = "Andrew Phoenix"

import eulib

top = 10000
x = 1
divisorsum = [0]
while x < top:
    g = sum(eulib.divisors(x)) - x
    divisorsum.append(g)
    x = x + 1
answer = 0
for i in range(top):
    print
    i, divisorsum[i]
    if divisorsum[i] < top:
        print
        'what ' + str(divisorsum[divisorsum[i]])
        if divisorsum[divisorsum[i]] < top:
            if divisorsum[i] != i:
                if divisorsum[divisorsum[i]] == i:
                    answer = answer + i
print
'the answer is ' + str(answer)
