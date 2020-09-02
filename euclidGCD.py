from math import *

def euclid_algo(x, y, verbose=True):
    if x < y:
        return euclid_algo(y, x, verbose)
    print()
    while y != 0:
        if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
        (x, y) = (y, x % y)

    if verbose: print('GCD is %s' % x)
    return x

a = int(input("Enter first number: "))
b = int(input("Enter second number "))
euclid_algo(a, b)