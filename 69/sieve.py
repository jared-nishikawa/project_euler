#!/usr/bin/python

def prime_sieve(n):
    primes = [2]
    for k in range(2,n):
        prime = True
        for p in primes:
            if k % p == 0:
                prime = False
                break
            if p > k**0.5:
                break
        if prime:
            primes.append(k)
    return primes

def phi_sieve(n):
    # phi of 0 1 2
    phi = range(n)
    phi[0] = 1
    phi[1] = 1
    for p in range(2,n):
        # Not initialized, must be prime
        if phi[p] == p:
            k = 1
            while k*p < n:
                phi[k*p] *= 1-1/float(p)
                k += 1
    return phi

if __name__ == '__main__':
    phi = phi_sieve(1000000)
    norm = [i/phi[i] for i in range(len(phi))]
    M = max(norm)
    i = norm.index(M)
    print i,M


