"""This is Problem 44 of ProjectEuler

Pentagonal numbers are generated with this formula:

Pentagonal              Pn=n(3n-1)/2             1, 5, 12, 22, 35, ...

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk  Pj| is minimised; what is the value of D?
"""
__author__ = "Andrew Phoenix"

import math

import eulib

top = 2167

for x in range(1, top):
    for y in range(x, top):
        if eulib.ispent(math.fabs(eulib.genpent(y) - eulib.genpent(x))):
            if eulib.ispent((eulib.genpent(y) + eulib.genpent(x))):
                print
                x, eulib.genpent(x), y, eulib.genpent(y), eulib.genpent(y) - eulib.genpent(x)
                break
