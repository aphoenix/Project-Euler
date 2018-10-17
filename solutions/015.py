"""This is Problem 15 of ProjectEuler

Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?"""

# It is important to note that the answer is actually fairly intuitive. It is the middle coefficient of the 20th row of Pascal's triangle.
# WOAH THERE COWBOY
# It's not actually the coefficient in the middle of the 20th row - it's the middle coefficient in the 40th row!
# Note that any coefficient of pascal's triangle can be written as (n!)/(n-k)!(k)!


import math

print
math.factorial(40) / (math.factorial(20)) ** 2
