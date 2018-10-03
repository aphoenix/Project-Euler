"""
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
"""

knownEnding = []
count = 0
#countIteration = 0
for i in range(10000001):
    knownEnding.append(-1)
    
"""
We will use method of memoization and dp to find the count as this will ensure
we will be at max see 10^7 values which gives our answer linear order
To check this uncomment lines having variable countIteration in it
"""
def sumDigitSquare(n):
    sum = 0
    while n:
        sum += (n%10)**2
        n = n//10
    return sum

def checkEnding(i):
    if knownEnding[i] is -1:
        #global countIteration
        #countIteration += 1
        knownEnding[i] = checkEnding(sumDigitSquare(i))
    return knownEnding[i]

knownEnding[1]=1
knownEnding[89]=89
count = 0
for i in range(1,10000001):
    if checkEnding(i) is 89:
        count+=1

print("count = ",count)
#print("countIteration = ",countIteration)
