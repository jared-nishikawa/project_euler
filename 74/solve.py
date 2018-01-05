#!/usr/bin/python

import math

chains = [0]*1000000

def populate(n):
    global chains
    orig = n
    chain = [n]
    while 1:
        n = get_next(n)
        if n in chain:
            break
        chain.append(n)
    chains[orig] = chain

def get_next(n):
    s = map(int, str(n))
    return sum(map(math.factorial,s))

if __name__ == '__main__':
    count = 0
    for i in range(1000000):
        if i % 100000 == 0:
            print i
        populate(i)

        if len(chains[i]) == 60:
            count += 1
    print count



