import numpy as np
import time
import random
import re
import datetime
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
    """
    Calculate the likely hood of a result of k given n dice with s sides. 
    """
    sumation = 0
    for i in range(0,  1+int( floor( ( k - n ) / float( s ) ) ) ):
        sumation += (-1)**i * choose( n, i ) * choose(k - s*i - 1, n - 1)
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
    # Catch any overflows gracefully, and tell the user. This might need to be changed for
    #   true library deployment. 
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

def dieroll(dice,sides):
    """
    Return a random result for the given number of dice with the given number of sides.
    """
    tmp = [random.randint(1,sides) for i in range(dice)]
    return sum(tmp),tmp

def diceeval(inStr="1d20"):
    """
    Evaluate a given basic math and dice string with python math notation. Currently dice 
    must be in the form of nDs where n is the number of dice, and s is the number of sides
    on each die. All dice rolls are evaluated before any math is evaluated.
    """
    matchInt = "((\d+)d(\d+))"
    match = re.search( matchInt, inStr )
    while( match ):
        dice = dieroll( int( match.group(2) ), int( match.group(3) ) )[0]
        inStr = re.sub( matchInt, str( dice ), inStr, count=1)
        match = re.search( matchInt, inStr )
    return eval(inStr)

def diePrompt():
    #preload it with something useful
    oldStr = "1d20"
    while(1):
        diceStr = raw_input("\n>")
        print datetime.datetime.fromtimestamp( time.time() ).strftime('%Y-%m-%d %I:%M:%S')
        if( not len( diceStr ) ):
            print "r:",oldStr
            diceStr = oldStr
        else:
            print "d:",diceStr
        oldStr = diceStr
        print diceeval(diceStr)

diePrompt()