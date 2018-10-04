"""
In 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
Find the last ten digits of this prime number.
"""
"""
Logic: (ac) % b = (a % b) * (c % b)
    (a + c) % b = (a % b) + (c % b)
"""

#Constants for question
a = 28433
b = 7830457
m = 10**10

modulo = []
for i in range(b+1):
    modulo.append(-1)
modulo[0] = 1
modulo[1] = 2

def powerOf2Mod(p,m):
    if modulo[p] is -1:
        modulo[p] = ( powerOf2Mod(p // 2,m) * (powerOf2Mod((p + 1) // 2,m))) % m
    return modulo[p]

print((a * powerOf2Mod(b,m))% m + 1)
