"""This is Problem 25 of ProjectEuler

Find the first fibonacci number with 1000 digits"""

__author__ = "Andrew Phoenix"

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]


# You could start this at one, but it's better to pick a more intelligent start

for x in range (4500, 4800):
  print x, ":", len(str(fib(x)))
  if len(str(fib(x))) > 999:
    break

