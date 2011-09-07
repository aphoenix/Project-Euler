"""A set of Number Theory functions, mostly intended for helping to solve Project Euler questions."""

__author__ = "Andrew Phoenix"

import math
import itertools
import operator

def ackermann(m,n):
    '''This prints out the ackermann number of (m,n) but it's not recommended to try doing more than 4,3.'''
    while m >= 4:
        if n == 0:
            n = 1
        else:
            n = ackermann(m, n - 1)
        m -= 1
    if m == 3:
        return (1 << n + 3) - 3
    elif m == 2:
        return (n << 1) + 3
    elif m == 1:
        return n + 2
    else: # m == 0
        return n + 1
def ackermod(i,j,mod):
    '''A modulo Ackermann function'''
    if i == 0:
        return (j+1)%mod
    if i > 0:
        if j == 0:
            return ackermod(i-1, j, mod)
        if j > 0:
            return ackermod(i-1, ackermod(i, j-1, mod), mod)
def dectobin(n):
    ''' convert decimal integer n to binary string bStr '''
    bStr = ''
    if n < 1:  
        return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr
def sieve(end):
    '''Using the sieve of aristhothenes to find all primes up to a given number (end) '''
    if end < 2: return []  
    lng = ((end/2)-1+end%2)  
    sieve = [True]*(lng+1)  
    for i in range(int(end**0.5) >> 1):  
        if not sieve[i]: continue  
        for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
            sieve[j] = False  
    primes = [2]  
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  
    return primes
def isprime(n):
    ''' Check if integer n is, in fact, prime '''
    for p in range (2, int(n**0.5)+1):
        if n%p==0:
            return False
    return True
def ispalindrome(x):
    ''' Checks to see if x is a palindrome number (reads the same forward and backwards) '''
    s=str(x)
    check=[c for c in s.lower()]
    return (check==check[::-1])
def sumofpower(x,y):
    ''' For each digit in x, raises to the power of y and sums them '''
    s=str(x)
    sum=0
    for c in s:
        sum+=(int(c))**y
    return sum
def ispandigital(x,n):
    ''' Checks to see if x uses all digits 1 .. n exactly once '''
    if n>9 or n<1:
        return FALSE
    if len(x) != n:
        return FALSE
    s=str(x)
    check=[c for c in s.lower()]
def inttolist(x):
    ''' Turns an int into a list of int, with each character of the int becoming a character in the list.'''
    s=str(x)
    longlist=[c for c in s]
    ints=[int(n) for n in longlist]
def mul(A, B):
    ''' Step 1 in a fast Fibonacci generator fib(n)'''
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f
def pow(A, n):
    ''' Step 2 in a fast Fibonacci generator fib(n)'''
    if n == 1:     
        return A
    if n & 1 == 0: 
        return pow(mul(A, A), n//2)
    else:          
        return mul(A, pow(mul(A, A), (n-1)//2))
def fib(n):
    ''' Generates the Nth fibonacci number.'''
    if n < 2: 
        return n
    return pow((1,1,0), n-1)[0]
def genhex(x):
    ''' Generate the nth Hexagonal Numbers'''
    return x*(2*x-1)
def genpent(x):
    ''' Generate the nth Pentagonal Numbers'''
    return x*(3*x-1)/2
def gentri(x):
    ''' Generate the nth Triangle Numbers'''
    return x*(x+1)/2
def ispent(x):
    ''' Check to see if a number is Pentagonal using the general solution to the quadratic formula and P(n)=n(3n-1)/2'''
    f=(1+(1+24*x)**0.5)/6
    g=math.floor(f)
    if f-g==0:
        return True
    else:
        return False
def istri(x):
    ''' Check to see if a number is Triangular using the general solution to the quadratic formula and T(n)=n(n+1)/2'''
    f=((1+8*x)**0.5-1)/2
    g=math.floor(f)
    if f-g==0:
        return True
    else: 
        return False
def hcf(x,y):  
    ''' Find the Highest Common Factor of X and Y using Euclid's Algorithm'''
    while x!=y:  
        if x>y:  
            x-=y  
        elif y>x:  
            y-=x  
    return x
def rpfgen(d):
    ''' Will find the Reduced Proper Fractions between 0 and 1 for a denominator depth of d'''
    rpfs=[[0,1,0],[1,1,1]]
    for x in range (1,d):
        for n in range (1,x):
            if hcf(n,x) == 1:
                rpfs.append([n,x,n/x])
    return rpfs.sort()
def spiralsum(n):
    '''Returns the sum of the diagonals of an n by n spiral (see question 28). Jeebus, n better be odd.'''
    if n%2 == 0:
        return 'broken'
    if n==1:
        return 1
    else:
        return 4*n**2-n-5*(n-1)+1 + spiralsum(n-2)
def sumfile(str):
    '''opens a file and sums the items in the file. Not a particularly useful function.  '''
    f=open(str,'r')
    sum=0
    for n in range (0,100):
        c=f.readline()
        d=c[0:20]
        print d
        sum=sum+int(d)
    return sum
def factors(x):
    '''Lists all prime factors of X, and allows duplicates.'''
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist
def factorGen(n):
    '''A Generator to find prime factors of a given number. Use it like this: "for i in factorGen(n):"'''
    loop=2
    while loop<=n:
        if n%loop==0:
            n/=loop
            yield loop
        else:
            loop+=1
def getMultiplicity(list):
    multiplicity = []
    for f in sorted(set(list)):
        multiplicity.append(list.count(f))
    m = [sorted(set(list)),multiplicity]
    return m
def divisors(n):
    '''Uses the factorGen and getMultiplicity to find divisors of n'''
    factors=getMultiplicity(list(factorGen(n)))
    primes=factors[0]
    multiplicities=factors[1]
    exponents = itertools.product(*(range(n + 1) for n in multiplicities))
    factors = (itertools.izip(primes, e) for e in exponents if sum(e) >= 2)
    divisors = [reduce(operator.mul, (p ** e for p, e in f)) for f in factors]
    divisors.extend(primes)
    divisors.append(1) 
    return divisors
def naivechampernowne(n):
    '''This builds the Champernowne Constant to the xth term.
    The higher (x) is the more accurate the constant will be.
    Note that this puts together three lengthy summations that are 
    broken down in previous functions.
    '''
    x = 0
    y = ''
    while len(y) < n:
        y += `x`
        x = x + 1
    return y


def champernowne(n):
    '''This is a better champernowne maker. Look at http://www.skymind.com/~ocrow/python_string/
    for more information. This is method 5.'''
    from cStringIO import StringIO
    file_str = StringIO()
    for num in xrange(n):
        file_str.write(`num`)
    return file_str.getvalue()


def mostCommon(lst):
    '''This will return the most common element of a list. May not be
    computationally optimal.'''
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]



if __name__=="__main__":
    print 'This is just a library. You probably want to help(eulib) if you want to see what it can do. And you probably want to include it in something else.'

