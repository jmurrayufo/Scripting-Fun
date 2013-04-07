import numpy as np
import time
from math import floor

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def F(s,n,k):

    # print 1+int( floor( ( k - n ) / float( s ) ) ) 
    sumation = 0

    for i in range(0,  1+int( floor( ( k - n ) / float( s ) ) ) ):
        sumation += (-1)**i * choose( n, i ) * choose(k - s*i - 1, n - 1)
        # print "Sum for",i
        # print (-1)**i
        # print choose( n, i )
        # print choose(k - s*i - 1, n - 1)
        # print sumation
    try:
        return sumation / float(s**n)
    except OverflowError:
        print "Error on: %d^%d"%(s,n)
        time.sleep(1)
        raise

def Fs(s,n,k):
    """
    Print the cumulative sumation of a result from n to k. This is the %% chance to get a 
    result of k or less
    """
    try:
        float(s**n)
    except OverflowError:
        print "Error on: %d^%d"%(s,n)
        print "Try a smaller value?"
        return
    sum = 0.0
    nmin = n
    nmax = min( k, s*n )
    for i in range( nmin, nmax+1 ):
        sum+=F(s,n,i)
    return sum