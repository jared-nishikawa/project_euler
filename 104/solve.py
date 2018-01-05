#!/usr/bin/python

def fib():
    A = 1
    B = 1
    k = 1
    while 1:
        A,B = A+B,A
        k += 1
        if ispan(B):
            break
    return k

def ispan(n):
    pan = list('123456789')
    s = str(n)
    if len(s) < 9:
        return False
    first = list(s[:9])
    last = list(s[-9:])
    first.sort()
    if first == pan and last == pan:
        return True
    return False



