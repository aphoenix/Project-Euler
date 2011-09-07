"""Project Euler 39

If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?


Discussion: To solve this, I did a bit of searching on wikipedia on
pythagorean triples. I think the quickest way to find a solution is to parse a
list of triples and see what the most common sum of the triples are.

"""


__author__="Andrew Phoenix"


import eulib


f=open('resources/triples.txt', 'r')
thesums=[]
for line in f:
    thisrow=line.split(',')
    onesum=(int(thisrow[0])+int(thisrow[1])+int(thisrow[2]))
    i=1
    total=onesum
    while (total<1000):
        total=onesum*i
        thesums.append(total)
        i=i+1


answer=eulib.mostCommon(thesums)
print thesums
print answer
