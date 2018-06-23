"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
Since last digit is 0,2nd last will also be 0
Now we are left with 8 blanks with a total possiblity of 10^8 numbers lets check which is perfect square
"""
from math import sqrt
digits = []
for digit in range(0,10):
    digits.append(digit)

number = 0
for i in range(1,10):
    number = number * 100 + i

def isSquare(n):
    #Two conditions for better handling round-off errors
    if sqrt(n)==sqrt(n)//1 and (int(sqrt(n))**2==n):
        return True

def singleDigitIterator(number,placeValue):
    if placeValue == 10 ** 17:
        return
    for digit in digits:
        num = number + digit * placeValue
        if(isSquare(num)):
            print(sqrt(num) * 10,num,num-sqrt(num)**2)
        else:
            singleDigitIterator(num,placeValue * 100)

#singleDigitIterator(number,10)

"""
METHOD - 2 

We can remove last 2 zeros now square has form 1_2_3_4_5_6_7_8_9
Since last digit of square is 9,its root can end only in 3 or 7
"""
maxPossibleSqaure = 19293949596979899
minPossibleSqaure = 10203040506070809
maxPossibleRoot = int(sqrt(maxPossibleSqaure))
minPossibleRoot = int(sqrt(minPossibleSqaure))
"""
There are 37892561 i.e. 4*10^7 possiblities but last digit can only be 3 or 7
so actual total possiblity in this method is about 8*10^6 which is faster than
singleDigitIterator method
"""
def checkPossibleSolution(n):
    m = n * n
    for i in range(9,0,-1):
        if not m%10 == i:
            return False
        m = m//100
    return True

def generateAllPossibleSolutions():
    for i in range(minPossibleRoot//10,maxPossibleRoot//10+1):
        for j in [3,7]:
            if checkPossibleSolution(i*10+j):
                return j*10 + i*100

print(generateAllPossibleSolutions())
