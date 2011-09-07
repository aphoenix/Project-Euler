"""Project Euler 22

Find the value of all names in the name file.

Sum the names, then multiply by position in file.

Note: I sanitized and sorted the list in vi."""

__author___ ="Andrew Phoenix"

f=open('resources/names.txt', 'r')
l=1
total=0
def findsum(name):
    sum=0
    for c in name:
        sum+=ord(c)-64
    return sum
def sanitize(filename):
    f=open(filename, 'r')
    for line in f:
        line.replace(' ','')
        names = line.split(',')
    return names
names=sanitize('resources/names.txt')
names.sort()
for name in names:
    name=name[1:-1]
    x=findsum(name)
    total=total+x*l
    l=l+1
    print total
