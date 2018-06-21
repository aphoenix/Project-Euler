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
#number *= 100

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

singleDigitIterator(number,10)
