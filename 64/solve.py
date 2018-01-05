#!/usr/bin/python

"""
sqrt(23) = 4 + sqrt(23) - 4

sqrt(23)-4 = 1/1/(sqrt(23)-4)
           = 1/((sqrt(23)+4)/7)
           = 1/((sqrt(23)+7-3)/7)
           = 1/(1 + (sqrt(23)-3/7))

(sqrt(23)-3)/7 = 1/(7/(sqrt(23)-3))
               = 1/
"""

import fractions

def get_first(n):
    return int(n**0.5)

# This is the form (sqrt(n) - x)/d
def get_next(n, x, d):
    # Rationalize the denominator
    D = (n - x**2)
    # d*(sqrt(n)+x)/D
    # Take integer part
    i = int(d*(n**0.5 + x)/D)
    # Simplify the leftovers
    F = fractions.Fraction(numerator=d, denominator=D)
    D_ = F.denominator
    new_x = x - i*D_
    new_d = D_
    return i, -new_x, new_d
    # (sqrt(n) -i*D) / D

# 23 --> [4;(1,3,1,8)]
def sqrt_continued(n):
    A = []
    a0 = get_first(n)
    x = a0
    d = 1
    for i in range(250):
        i,x,d = get_next(n,x,d)
        A.append(i)
    return A

def detect_period(n):
    A = sqrt_continued(n)

    for p in range(1, 250):
        # Organize in columns
        cols = [A[i::p] for i in range(p)]
        checks = [all(map(lambda x: x == col[0], col)) for col in cols]
        if all(checks):
            return len(checks)

if __name__ == '__main__':
    odd = []
    for n in range(2,10001):
        if n**0.5 == int(n**0.5):
            continue
        P = detect_period(n)
        try:
            if P % 2 == 1:
                odd.append(n)
        except:
            print n
            exit()
    print len(odd)




