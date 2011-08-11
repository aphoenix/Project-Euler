"""A traversal library for stepping through files and stuff."""

__author__ = "Andrew Phoenix"

import math


def triangle(filename):
    f = open(filename, 'r')
    row = 1
    biggest = []
    cur = ['0']
    for line in f:
        # take the values from the line and put them in a list
        cur = line.split()
        # max(row,col) = [max(row-1,col)+(row,col)] OR [max(row-1,col-1)+(row,col)] whichever is greater.
           



if __name__=="__main__":
    print 'This is a library. Just inlcude it, or use help(traverse)'
