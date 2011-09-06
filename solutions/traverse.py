"""A traversal library for stepping through files and stuff."""


__author__ = "Andrew Phoenix"


import math


def triangle(filename):
    '''triangle(filename) will open [filename] and find the best path through
    assuming that it is a text file as given in the project euler question.'''
    f = open(filename, 'r')
    cur = []
    total = [0]
    for line in f:
        # take the values from the line and put them in a list
        cur = line.split()
        row = len(cur)
        if row == 1:
            maxi = cur
        else:
            maxi = []
            maxi.append(int(total[0])+int(cur[0]))
            for n in range(1, row-1):
                if (int(total[n])>int(total[n-1])):
                    maxi.append(int(cur[n])+int(total[n]))
                else:
                    maxi.append(int(cur[n])+int(total[n-1]))
            maxi.append(int(cur[row-1])+int(total[row-2]))
        total = maxi
    print max(total)
        

if __name__=="__main__":
    print 'This is a library. Just include it, or use help(traverse)'
