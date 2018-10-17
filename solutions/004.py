"""This is Problem 4 of ProjectEuler

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers."""

__author__ = "Andrew Phoenix"


def ispalindrome(x):
    '''Checks to see if x is a palindrome number'''
    s = str(x)
    check = [c for c in s.lower()]
    return (check == check[::-1])


for x in range(900, 999):
    for y in range(900, 999):
        if ispalindrome(x * y):
            print
            x * y
