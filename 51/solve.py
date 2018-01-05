#!/usr/bin/python

"""
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the
same digit, this 5-digit number is the first example
having seven primes among the ten generated numbers,
yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

import time
import itertools

def stopwatch(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print end-start
    return result

# This takes about 2 seconds
def get_primes():
    with open('../primes.txt') as f:
        primes = map(int, f.readlines())
    return primes

def make_families(top):
    families = {}
    digits = "0123456789*"
    for i in range(1, top):
        for comb in itertools.combinations_with_replacement(digits, i):
            for perm in itertools.permutations(comb):
                if perm[0] == "0":
                    continue
                perm = ''.join(perm)
                if '*' in perm:
                    families[perm] = {}
    return families

def zipper(A, B):
    A = list(A)
    B = list(B)
    items = []
    while 1:
        items += A[0]
        del A[0]
        if not A:
            break
        items += B[0]
        del B[0]
    return items

# i is a digit
# s is a prime (in string form)
# b is a pattern containing i and *
def stitch(i, s, b):
    spl = s.split(i)
    assert len(spl) == len(b) + 1
    zippered = ''.join(zipper(spl,b))
    return zippered

def get_families(s, i):
    if i not in s:
        return []
    my_fams = []
    num = s.count(i)
    for k in range(2**num):
        b = bin(k)[2:]
        b = pad(b, num, fromleft=True)
        b = b.replace('0','*')
        b = b.replace('1', i)
        f = stitch(i, s, b)
        if '*' in f:
            my_fams.append(f)
    return my_fams

def pad(s, length, char='0', fromleft=False):
    while len(s) < length:
        if fromleft:
            s = char + s
        else:
            s += char
    return s

def main():
    #F = make_families(9)
    F = {}
    primes = get_primes()

    for prime in primes[:100000]:
        s = str(prime)
        for i in set(s):
            M = get_families(s,i)
            for t in M:
                if not F.has_key(t): 
                    F[t] = {}
                F[t][prime] = 1
    for k in F.keys():
        v = F[k]
        if len(v) >= 8:
            print k
            primes = v.keys()
            primes.sort()
            print primes[0]




    

if __name__ == '__main__':
    main()
