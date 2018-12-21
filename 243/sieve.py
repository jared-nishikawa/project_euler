from operator import mul
from functools import reduce
import itertools

if __name__ == '__main__':
    #composites = [4,6,8,9,10,12,14,15,16,18,20,21,22]
    decomps = [(2,2), (2,3), (2,2,2), (3,3), (2,5), (2,2,3),
            (2,7), (3,5), (2,2,2,2), (2,3,3), (2,2,5), (3,7), (2,11)]

    primes = [2,3,5,7,11,13,17,19,23]
    n = reduce(mul, primes)
    phi = reduce(mul, [p-1 for p in primes])
    threshold = 15499/94744
    print(phi/(n-1) < threshold)
    for decomp in decomps:
        comp = reduce(mul, decomp)
        ph = reduce(mul, [p-1 for p in decomp])
        
        new_n = n*comp
        new_phi = phi*ph
        f = new_phi/(new_n-1)
        #print(f"{new_n}: {new_phi}/{new_n-1}")
        print(f"{new_n}: {f < threshold}")

