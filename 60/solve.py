#!/usr/bin/python

"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in
any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which
any two primes concatenate to produce another prime.
"""

PRIMES = {}

def get_primes():
    global PRIMES
    with open('../primes.txt') as f:
        for line in f:
            prime = int(line)
            PRIMES[prime] = 1

def is_prime(n):
    return PRIMES[n] if PRIMES.has_key(n) else 0

if __name__ == '__main__':
    pass


